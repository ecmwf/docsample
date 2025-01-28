import argparse
from .core import hello


def get_parser():
    parser = argparse.ArgumentParser(description="CLI for docsample library")
    parser.add_argument("input", type=str, help="Input string to process.")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    print(hello(args.input))


if __name__ == "__main__":
    main()
