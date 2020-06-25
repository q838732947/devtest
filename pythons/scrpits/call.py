import os


def terminals(command):
    os.system(command=command)


def path_join(path_list):
    return os.path.join(*path_list)


def get_path():
    return os.getcwd()


def get_filelist(folder) -> list:
    return os.listdir(folder)


def compare_two_folder_is_same(folder1, folder2):
    folder1 = get_filelist(folder1)
    folder2 = get_filelist(folder2)
    # print(folder1)
    # print(folder2)
    common = [x for x in folder1 if x in folder2]
    diff = [y for y in (folder1 + folder2) if y not in common]
    # print(common)
    # print(diff)
    if not diff:
        return True
    return False


def check_file_exist(filepath):
    return os.path.exists(filepath)


def file_not_exists_then_makedir(filepath):
    if check_file_exist(filepath):
        print(f"{filepath}file is exist")
        return
    else:
        try:
            os.mkdir(filepath)
            print(f"create folder {filepath}")
        except FileNotFoundError:
            os.makedirs(filepath)
            print(f"create folders {filepath}")


def with_open(filepath, mode='r'):
    with open(filepath, mode) as f:
        return f.read()


def main():
    # command = "python useargparse.py -t -s string -c"
    # terminals(command)
    # print(path_join([get_path(), "demo"]))
    folder1 = path_join([get_path(), "demo", "222", "0.txt"])
    folder2 = path_join([get_path(), "demo", "222"])
    # print(compare_two_folder_is_same(folder1, folder2))
    # print(check_file_exist(folder1))
    # file_not_exists_then_makedir(folder1)
    f = with_open(folder1)


if __name__ == '__main__':
    pass
    main()
