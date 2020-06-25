import argparse


def func1(args):
    print(f"my school is {args.school}")
    print(f"my a is {args.a}")
    print(f"my gender is P{args.gender}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('school')
    parser.add_argument('-a', required=True)
    parser.add_argument('--male', default="man", choices=['man', 'women'], dest='gender')
    args = parser.parse_args()
    func1(args)


if __name__ == '__main__':
    main()
