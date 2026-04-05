import hashlib

def hash_variant(lines):
    variant_str = "\n".join(lines)
    variant_str = variant_str + '\n'
    return hashlib.sha256(variant_str.encode()).hexdigest()

def make_variant(lines, n):
    variant = lines.copy()
    for i in range(len(lines)):
        variant_check = (n >> i) & 1
        if variant_check == 1:
            variant[i] = variant[i] + " "
    return variant