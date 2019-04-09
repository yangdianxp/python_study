
try:
    file_read = open("README")
    file_write = open("README.copy", "w")

    while True:
        text = file_read.readline()
        if not text:
            break
        file_write.write(text)

    file_read.close()
    file_write.close()
except Exception as result:
    print(result)