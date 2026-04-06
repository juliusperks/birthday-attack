import find_collision
import argparse
import subprocess

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
    num_suffix_chars = args.digits  # Number of characters from the hash suffix to use for collision detection
    real_table = find_collision.build_table(real_confession, max_lines=args.lines, num_suffix_chars=num_suffix_chars, label="real")
    fake_table = find_collision.build_table(fake_confession, max_lines=args.lines, num_suffix_chars=num_suffix_chars, label="fake")
    print("Finding collision...")
    collision = find_collision.find_collision(real_table, fake_table)
    if collision:
        real_variant, fake_variant = collision
        print("Collision found!")
        print("Outputting variants to files to output/...")
        content = "\n".join(real_variant) + "\n"
        with open("output/"+"output_real.txt", "wb") as f:
            f.write(content.encode("ascii"))
        content = "\n".join(fake_variant) + "\n"
        with open("output/"+"output_fake.txt", "wb") as f:
            f.write(content.encode("ascii"))
        result = subprocess.run(["shasum", "-a", "256", "output/output_real.txt", "output/output_fake.txt"], capture_output=True, text=True)
        print(result.stdout)
    else:
        print("No collision found.")


if __name__ == "__main__":
    main()