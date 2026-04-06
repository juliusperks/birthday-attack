import hasher

def build_table(lines, max_variants=2**16, num_suffix_chars=2):
    table = {}
    lines = lines[:16] # Cap the analysis to 16 lines. 
    for n in range(min(2 ** len(lines), max_variants)):
        if n % 10000 == 0:
            print(f"Building table: {n} / {min(2 ** len(lines), max_variants)} variants processed...")
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
            print(f"Searching: {i/total*100:.0f}%")
        if suffix in real_table:
            print(f"Collision found on suffix: ...{suffix}")
            return real_table[suffix], fake_table[suffix]
    return None