import find_collision

file_path = './confessions/'


def load_lines(filepath):
    with open(filepath, 'r') as f:
        return f.read().splitlines()

def main():
    real_confession = load_lines(file_path+'confession_real.txt')
    fake_confession = load_lines(file_path+'confession_fake.txt')
    real_table = find_collision.build_table(real_confession)
    fake_table = find_collision.build_table(fake_confession)
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