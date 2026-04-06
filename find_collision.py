import hasher
import logger

def build_table(lines, max_lines, num_suffix_chars=2, label=""):
    table = {}
    lines = lines[:max_lines] # Cap the analysis to max_lines lines.
    for n in range(2 ** len(lines)):
        if n % 10000 == 0:
            logger.log(f"Building table [{label}]: {n} / {2 ** len(lines)} variants processed...")
        variant = hasher.make_variant(lines, n)
        h = hasher.hash_variant(variant)
        suffix = h[-num_suffix_chars:]
        if suffix not in table:
            table[suffix] = []
        table[suffix] = variant
    return table

def find_collision(real_table, fake_table):
    total = len(fake_table)
    interval = max(1, total // 100)
    for i, (suffix, variants) in enumerate(fake_table.items()):
        if i % interval == 0:
            logger.log(f"Searching: {i/total*100:.0f}%")
        if suffix in real_table:
            logger.log(f"Collision found on suffix: ...{suffix}")
            return real_table[suffix], fake_table[suffix]
    return None