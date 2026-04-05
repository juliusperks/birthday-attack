import hasher

def build_table(lines):
    table = {}
    for n in range(2 ** len(lines)):
        variant = hasher.make_variant(lines, n)
        h = hasher.hash_variant(variant)
        suffix = h[-2:]
        if suffix not in table:
            table[suffix] = []
        table[suffix] = variant
    return table

def find_collision(real_table, fake_table):
    for suffix, variants in fake_table.items():
        if suffix in real_table:
            return real_table[suffix], fake_table[suffix]
    return None