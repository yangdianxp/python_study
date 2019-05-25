import traceback
import os
import sys
import zipfile

def main():
    #查找文件名
    os.chdir(r"C:\Users\Administrator\Desktop\za20190525")
    for root, dirs, files in os.walk("."):
        for f in files:             
            unzip = zipfile.ZipFile(f)
            for u in unzip.namelist():
                unzip.extract(u, ".")
                print('uncompressing {} finished'.format(u))
            unzip.close()
            os.remove(f)
            
if __name__ == '__main__':
    try:
        main()
    except Exception as result:
        ex_type, ex_val, ex_stack = sys.exc_info()
        print(ex_type)
        print(ex_val)
        for stack in traceback.extract_tb(ex_stack):
            print(stack)

