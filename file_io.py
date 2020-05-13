my_file_handle = None
try:
    my_file_handle = open("GarbageCollector_readme_en.txt", "r")

    my_file_handle.read()

    # Use print to print the line else will remain in buffer and replaced by next statement
    print(my_file_handle.readline())

    # outputs first two characters of next line
    print(my_file_handle.readline(2))

    my_file_handle = open("D:\\_ARIEL\\MyLessons\\PYTHON\\Lesson6\\GarbageCollector_readme_en.txt", "r")
    my_file_handle.read()
    for line in my_file_handle:
        print(line)
    my_file_handle.close()


    # my_file=open("D:\\new_dir\\multiplelines.txt","r")
    # my_file.readlines()

    my_file_handle = open("changelog.txt")
    my_file_handle.read()
    my_file_handle = open("D:\\_ARIEL\\MyLessons\\PYTHON\\Lesson5\\python_course2020_lesson5\\JUST_FILE.txt", mode="w", encoding="utf-8")
    my_file_handle.write("Writing to a new file1\n")
    my_file_handle.write("Writing to a new file2\n")
    my_file_handle.write("Writing to a new file3\n")
    my_file_handle.close()

    fruits=["Orange\n","Banana\n","Apple\n"]
    new_file=open("D:\\_ARIEL\\MyLessons\\PYTHON\\Lesson5\\python_course2020_lesson5\\JUST_FILE.txt",mode="a+",encoding="utf-8")
    new_file.writelines(fruits)
    for line in new_file:
        print(line)
    new_file.close()

    # seek(0)
    cars = ["Audi\n", "Bentely\n", "Toyota\n"]
    new_file = open("D:\\_ARIEL\\MyLessons\\PYTHON\\Lesson5\\python_course2020_lesson5\\newfile.txt", mode="a+", encoding="utf-8")
    for car in cars:
        new_file.write(car)
    print("Tell the byte at which the file cursor is:", new_file.tell())
    new_file.seek(0)
    for line in new_file:
        print(line)
    # ==============
    cars = ["Audi\n", "Bentely\n", "Toyota\n"]
    new_file = open("D:\\_ARIEL\\MyLessons\\PYTHON\\Lesson5\\python_course2020_lesson5\\newfile.txt", mode="a+", encoding="utf-8")
    for car in cars:
        new_file.write(car)
    print("Tell the byte at which the file cursor is:", new_file.tell())
    new_file.seek(0)
    for line in new_file:
        print(line)
    new_file.seek(4, 0)
    print(new_file.readline())
    new_file.close()

except FileNotFoundError as err:
    print(f"OS error: {err}")


except IOError:
    print("File not found or path is incorrect")
finally:
    if my_file_handle is not None:
        my_file_handle.close()
    print("exit")