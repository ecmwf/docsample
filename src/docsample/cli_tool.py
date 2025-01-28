import argparse
from .core import hello_world


def main():
    parser = argparse.ArgumentParser(description="CLI for docsample library")
    parser.add_argument("input", type=str, help="Input string to process.")
    args = parser.parse_args()
    print(hello_world(args.input))


if __name__ == "__main__":
    main()
