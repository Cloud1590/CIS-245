def main():
    file_name = input("Enter the name of the file: ")
    name = input("Enter your name: ")
    address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")

    file = open(file_name, "w")
    file.write(name + ", " + address + ", " + phone_number + "\n")
    file.close()

    file = open(file_name, "r")
    line = file.readline()
    while line != "":
        print(line)
        line = file.readline()
    file.close()


main()