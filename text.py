import os


def readFile():
    try:
        fhand = open('mtext.txt', 'r', encoding="UTF-8")
        print(fhand.read())
        fhand.close()
    except:
        print("error!")
        quit()


# end


def count_line():
    fhand = open("mtext.txt")
    count = 0
    for line in fhand:
        count = count + 1
    print('Line count: ', count)


def main():
    print("read the file:")
    print("*" * 10)
    readFile()
    count_line()
    find_from()
    print("*" * 10)


# end
def find_from():
    fhand = open("mtext.txt")
    for line in fhand:
        if line.startswith("From:"):
            print(line)


if __name__ == "__main__":
    main()
