#create a filede


def countLine():
    with open('data.txt', 'r') as file:

        count = 0

        for line in file:

            count += 1

    print(count)
def createFile():
    try:
        print("write file content :")
        fhand = open('data.txt','w',encoding="UTF-8")
        s = input(">")
        while s.lower() != "done":
            fhand.write(s+'\n')
            s = input(">")
        print("write successfull")
        fhand.close()
    except:
        print("Error!")
#end
def ReadFile():
    try:
        fhand = open("data.txt",'r',encoding="UTF-8")
        for str in fhand :
            print(str.rstrip())
        fhand.close()
    except:
        print("Error")
        quit()

def main():

    countLine()

if __name__ == '__main__':
    main()