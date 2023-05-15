import os
manual = input("Do you want to see manual? Type y for yes or n for no: ").lower()
if manual == "y":
    f = open("manual.txt", "r")
    print(f.read())
    convert = input("Type y for converting or n for to stop: ").lower()
    if convert == "y":
        input_file = input("enter the file path or name with extension: ")
        output_file = input("enter the output filename with extension: ")
        out = os.system(f"ffmpeg -i {input_file} {output_file}")
    else:
        print("You stopped the conversion...")
elif manual == "n":
    convert = input("Type y for converting or n for to stop: ").lower()
    if convert == "y":
        input_file = input("enter the file path or name with extension: ")
        output_file = input("enter the output filename with extension: ")
        out = os.system(f"ffmpeg -i {input_file} {output_file}")
    else:
        print("You stopped the conversion...")
