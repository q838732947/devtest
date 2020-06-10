import os


# sys.path.append("..")


def create_folder(dirname):
    os.makedirs(dirname)


def create_file(file):
    with open(file, "w") as f:
        s = "123"
        f.write(s)


def dirlist(dirname):
    print(os.walk(dirname))
    for maindir, subdir, file_name_list in os.walk(dirname):
        print("1:", maindir)  # 当前主目录
        print("2:", subdir)  # 当前主目录下的所有目录
        print("3:", file_name_list)  # 当前主目录下的所有文件


def get_filelist(folder) -> list:
    for maindir, subdir, file_name_list in os.walk(folder):
        return file_name_list


if __name__ == '__main__':
    pass
    folder1 = "111"
    # create_folder("111")
    folder2 = "222"
    # create_folder("222")
    # for i in range(10):
    #     create_file(folder+"/"+str(i)+".txt")
    l1 = get_filelist(folder1)
    l2 = get_filelist(folder2)
    common = [x for x in l1 if x in l2]
    print(common)
    diff = [y for y in l1 + l2 if y not in common]
    print(diff)
    diff = list(set(l1) ^ set(l2))
    print(diff)
