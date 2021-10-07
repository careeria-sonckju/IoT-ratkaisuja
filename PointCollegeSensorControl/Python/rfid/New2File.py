import sys

def subroutine(arg1):
    name = arg1
    print ("sub-rutiinista: "+name)

    file = open("test.txt", "w")
    file.write(name+"\n")
    file.close()

    file = open("test.txt", "r")
    name = file.readline()
    print("tiedostoluvusta: "+name)
    file.close()

def main(arguments):
    if len(arguments) == 1:
        print("main-rutiinista: "+arguments[0])
        subroutine(arguments[0])
    else:
        print ("You must supply one parameter")

if __name__ == "__main__":
    main(sys.argv[1:])