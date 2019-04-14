import os
import multiprocessing
import time

def copy_file(q, file_name, old_folder_name, new_folder_name):
    try:
        #print(file_name, old_folder_name, new_folder_name)
        old_f = open(old_folder_name + "\\" + file_name, "rb")
        content = old_f.read()
        old_f.close()
        new_f = open(new_folder_name + "\\" + file_name, "wb")
        new_f.write(content)
        new_f.close()
        q.put(file_name)
    except Exception as result:
        print(result)

def main():
    old_folder_name = input("请输入要copy的文件夹的名字:")
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass
    file_names = os.listdir(old_folder_name)
    #print(file_names)

    po = multiprocessing.Pool(5)

    q = multiprocessing.Manager().Queue()

    for file_name in file_names:
        po.apply_async(copy_file, (q, file_name, old_folder_name, new_folder_name))

    po.close()

    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        copy_ok_num += 1
        #print(file_name)
        print("\r进度:{}".format(copy_ok_num / all_file_num), end="")
        if copy_ok_num >= all_file_num:
            break
    print()

if __name__ == "__main__":
    main()