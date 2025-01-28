import argparse
from .core import hello


def main():
    parser = argparse.ArgumentParser(description="CLI for docsample library")
    parser.add_argument("input", type=str, help="Input string to process.")
    args = parser.parse_args()
    print(hello(args.input))


if __name__ == "__main__":
    main()
