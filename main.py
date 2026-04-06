import find_collision
import argparse
import subprocess
import time
import logger

file_path = './confessions/'


def load_lines(filepath):
    with open(filepath, 'r') as f:
        return f.read().splitlines()

def main():
    start = time.time()
    argparser = argparse.ArgumentParser(description='Birthday attack on confessions.')
    argparser.add_argument('--lines', type=int, default=16, help='number of lines to analyze from each confession (default: 16)')
    argparser.add_argument('--digits', type=int, default=2, help='number of hash suffix digits to use for collision detection (default: 2)')
    args = argparser.parse_args()
    logger.setup_log_file()

    logger.log("Loading confessions...")
    logger.log(f"Using {args.lines} lines from each confession and {args.digits} hash suffix digits for collision detection.")
    real_confession = load_lines(file_path+'confession_real.txt')
    fake_confession = load_lines(file_path+'confession_fake.txt')
    logger.log("Building hash tables...")
    num_suffix_chars = args.digits  # Number of characters from the hash suffix to use for collision detection
    t = time.time()
    real_table = find_collision.build_table(real_confession, max_lines=args.lines, num_suffix_chars=num_suffix_chars, label="real")
    logger.log(f"Real table built in {time.time() - t:.2f}s")

    t = time.time()
    fake_table = find_collision.build_table(fake_confession, max_lines=args.lines, num_suffix_chars=num_suffix_chars, label="fake")
    logger.log(f"Fake table built in {time.time() - t:.2f}s")

    logger.log("Finding collision...")
    t = time.time()
    collision = find_collision.find_collision(real_table, fake_table)
    logger.log(f"Collision search completed in {time.time() - t:.2f}s")

    if collision:
        real_variant, fake_variant = collision
        logger.log("Collision found!")
        logger.log("Outputting variants to files to output/...")
        content = "\n".join(real_variant) + "\n"
        with open("output/"+"output_real.txt", "wb") as f:
            f.write(content.encode("ascii"))
        content = "\n".join(fake_variant) + "\n"
        with open("output/"+"output_fake.txt", "wb") as f:
            f.write(content.encode("ascii"))
        result = subprocess.run(["shasum", "-a", "256", "output/output_real.txt", "output/output_fake.txt"], capture_output=True, text=True)
        logger.log(result.stdout)
    else:
        logger.log("No collision found.")
    logger.log(f"Completed in {time.time() - start:.2f}s")


if __name__ == "__main__":
    main()