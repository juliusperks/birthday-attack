import find_collision
import argparse

file_path = './confessions/'


def load_lines(filepath):
    with open(filepath, 'r') as f:
        return f.read().splitlines()

def main():
    argparser = argparse.ArgumentParser(description='Birthday attack on confessions.')
    argparser.add_argument('--lines', type=int, default=16, help='number of lines to analyze from each confession (default: 16)')
    argparser.add_argument('--digits', type=int, default=2, help='number of hash suffix digits to use for collision detection (default: 2)')
    args = argparser.parse_args()
    print("Loading confessions...")
    real_confession = load_lines(file_path+'confession_real.txt')
    fake_confession = load_lines(file_path+'confession_fake.txt')
    print("Building hash tables...")
    max_variants = 2**args.lines  # Limit the number of variants to generate for performance
    num_suffix_chars = args.digits  # Number of characters from the hash suffix to use for collision detection
    real_table = find_collision.build_table(real_confession, max_variants=max_variants, num_suffix_chars=num_suffix_chars)
    fake_table = find_collision.build_table(fake_confession, max_variants=max_variants, num_suffix_chars=num_suffix_chars)
    print("Finding collision...")
    collision = find_collision.find_collision(real_table, fake_table)
    if collision:
        real_variant, fake_variant = collision
        print("Collision found!")
        print("Real variant:")
        print("\n".join(real_variant))
        print("Fake variant:")
        print("\n".join(fake_variant))
    else:
        print("No collision found.")


if __name__ == "__main__":
    main()