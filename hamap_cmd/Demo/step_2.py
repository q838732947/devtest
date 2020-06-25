import argparse


def func2(args):
    print('simple_value     =', args.school)
    print('constant_value   =', args.constant_value)
    print('boolean_switch   =', args.boolean_switch)
    print('collection       =', args.collection)
    print('const_collection =', args.const_collection)
    print('nnn              =', args.nnn)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', action='store', dest='school',
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

    args = parser.parse_args()
    func2(args)


if __name__ == '__main__':
    main()
