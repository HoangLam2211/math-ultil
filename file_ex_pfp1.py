# Write a program that allows users to input data from the keyboard until enter “done” and data stored to file named
# data.txt then shows file’s content on the screen


def create_file():
    try:
        print('Input data : ')
        fhand = open("data.txt",'w',encoding='UTF-8')
        s = input('>')
        while s.lower() != 'done':
            fhand.write(s+"\n")
            s = input(">")
        print('write complete!')
        fhand.close()
    except:
        print('Error!')
        quit()
#end


def readfile():
    try:
        print("this is the text:")
        fhand = open('data.txt','r',encoding='UTF-8')
        for char in fhand :
            print(char.strip())
        fhand.close()
    except:
        print('Error')
        quit()

def main():
    create_file()
    readfile()

if __name__ == '__main__':
    main()

