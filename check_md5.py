# @Author  : TRY
# @Time    : 2021/02/26
# @Function:
import argparse
import os
import hashlib
# end

def make_md5(full_path, save=None, abs_path=None, pt=True):
    with open(full_path, "rb") as f:
        data = f.read()
        md5 = hashlib.md5(data).hexdigest()
        if pt:
            print('%s %s' % (md5, full_path))
        if save is not None:
            with open(save, "a") as t:
                t.write('%s %s\n' % (md5, full_path.replace(abs_path, "*")))
        return md5


def read_file(md5_file, check_path):
    with open(md5_file, "r") as f:
        while True:
            data = f.readline()
            if data:
                md5, path = data.split("*")
                md5, path = md5.strip(" "), path.strip("\n").strip("\\")
                file_path = os.path.join(check_path, path)
                if os.path.isfile(file_path):
                    if md5.strip(" ") != make_md5(file_path, pt=False):
                        print(file_path)
                        print("%s -md5 not equal" % path)
                else:
                    print(file_path)
                    print("%s -file loss" % path)
            else:
                break


def traverse_file(original_path, save_file, type_list, exclude_path, pt=False):
    for filepath, dirnames, filenames in os.walk(original_path):
        if exclude_path:
            for i in exclude_path.split(','):
                if i in dirnames:
                    dirnames.remove(i)
        for filename in filenames:
            if type_list is not None:
                end_with = filename.split(".")[-1]
                if end_with in type_list:
                    full_path = os.path.join(filepath, filename)
                    make_md5(full_path, save_file, original_path, pt)
            else:
                full_path = os.path.join(filepath, filename)
                make_md5(full_path, save_file, original_path, pt)


def check_md5(original_path, compare_path, save, type, exclude_path):
    # file to file
    if os.path.isfile(original_path):
        if compare_path is not None:
            if os.path.isfile(compare_path):
                print("check_result:", make_md5(original_path) == make_md5(compare_path))
                return
            else:
                print("path compare with path or file compare with file!")
                print("do not support path compare with file!")
                return
        else:
            make_md5(original_path)
            return
    elif os.path.isdir(original_path):
        if type is not None:
            type_list = type.split(",")
        else:
            type_list = None

        if save is not None:
            if os.path.isfile(save):
                os.remove(save)

        if os.path.isfile(temp_file):
            os.remove(temp_file)

        if compare_path is not None:
            # path to path
            if os.path.isdir(compare_path):
                # create md5 file
                traverse_file(original_path, temp_file, type_list, exclude_path)
                read_file(temp_file, compare_path)

                if os.path.isfile(temp_file):
                    os.remove(temp_file)
                return
                    # path to file
            elif os.path.isfile(compare_path):
                return read_file(compare_path, original_path)
            else:
                print("-c input is not real path or file!")
                return
        else:
            # only check
            traverse_file(original_path, save, type_list, exclude_path, True)
            return

    else:
        print("-o input is not real path or file!")
        return


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--original_path", required=True,
                    help="input original path, must input")
    ap.add_argument("-c", "--compare_path", required=False,
                    help="input compare path or check.text")
    ap.add_argument("-s", "--save", required=False,
                    help="save compared result as c heck.txt")
    ap.add_argument("-t", "--type", required=False,
                    help="check file type, exp: -t dll,lib")
    ap.add_argument("-e", "--exclude_path", required=False,
                    help="do not check path like log dir")
    kwargs = vars(ap.parse_args())
    # display a friendly message to the user
    temp_file = "temp.txt"
    check_md5(**kwargs)

