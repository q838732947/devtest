# 非常实用的初学教程
# https://blog.csdn.net/qq_36653505/article/details/83788460

# 创建 ArgumentParser() 对象
# 调用 add_argument() 方法添加参数
# 使用 parse_args() 解析添加的参数
# parser = argparse.ArgumentParser(description='manual to this script')
# parser.add_argument("hello", type=str, help="no -try")
# parser.add_argument("-a", type=str, help="this is test a")
# parser.add_argument("--b", type=str, default="")
# args = parser.parse_args()
# print(args.a)
# print(args.b)
# print(args.hello)
# parser = argparse.ArgumentParser()
# parser.add_argument('echo')     # add_argument()指定程序可以接受的命令行选项
# args = parser.parse_args()      # parse_args()从指定的选项中返回一些数据
# print(args)
# print(args.echo)
# parser = argparse.ArgumentParser(description = 'this is a description')
# parser.add_argument('--ver', '-v', action = 'store_true', help = 'hahaha')
# # 将变量以标签-值的字典形式存入args字典
# args = parser.parse_args()
# if args.ver:
#     print("Ture")
# else:
#     print("False")
import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', action='store', dest='simple_value',
                        help='Store a simple value')

    parser.add_argument('-c', action='store_const', dest='constant_value',
                        const='value-to-store',
                        help='Store a constant value')

    parser.add_argument('-t', action='store_true', default=False,
                        dest='boolean_switch',
                        help='Set a switch to true')
    parser.add_argument('-f', action='store_false', default=False,
                        dest='boolean_switch',
                        help='Set a switch to false')

    parser.add_argument('-a', action='append', dest='collection',
                        default=[],
                        help='Add repeated values to a list')

    parser.add_argument('-A', action='append_const', dest='const_collection',
                        const='value-1-to-append',
                        default=[],
                        help='Add different values to list')
    parser.add_argument('-B', action='append_const', dest='const_collection',
                        const='value-2-to-append',
                        help='Add different values to list')

    # nargs=2，表示-n后面需要2个参数，nargs='+'表示后面需要至少1个参数，nargs='?'表示后面需要0个或1个参数
    parser.add_argument('-n', action='store', nargs='+', dest='nnn')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    results = parser.parse_args()
    pppp(results)


def pppp(results):
    print('simple_value     =', results.simple_value)
    print('constant_value   =', results.constant_value)
    print('boolean_switch   =', results.boolean_switch)
    print('collection       =', results.collection)
    print('const_collection =', results.const_collection)
    print('nnn              =', results.nnn)

    # python useargparse.py -t -s string -c
    # -a aa -a bb -n n1 n2


if __name__ == '__main__':
    main()
