def main():
    num = int(input("please input some num:"))
    print("*" * num)

def foo():
    print("foo111")

import sys

if __name__ == '__main__':
    # main()
    for i in sys.path:
        print(i)