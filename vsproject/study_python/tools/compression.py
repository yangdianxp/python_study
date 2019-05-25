import traceback
import os
import sys
import zipfile

zip_file_base_name = "za"
count = 0

def main():
    #查找文件名
    os.chdir(r"F:\视频\za20190525")
    for root, dirs, files in os.walk("."):
        for f in files:
            global count       
            zip_name = "{}{:0>3d}{}".format(zip_file_base_name, count, ".zip")
            count += 1
            zip = zipfile.ZipFile( zip_name, 'w', zipfile.ZIP_DEFLATED )
            zip.write(f)
            zip.close()
            os.remove(f)
            print('compressing {} finished'.format(zip_name))

if __name__ == '__main__':
    try:
        main()
    except Exception as result:
        ex_type, ex_val, ex_stack = sys.exc_info()
        print(ex_type)
        print(ex_val)
        for stack in traceback.extract_tb(ex_stack):
            print(stack)

