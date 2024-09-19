def takeInput():
    try:
        noftri = int(input())
    except ValueError:
        print("Bro r u serious, give a number")
    try:
        values = input()
        lint = values.split(" ")
    except TypeError:
        print("Number of arguments not matched")
    return noftri,lint

def triangle(row):
    start = 65
    for i in range(row):
        j = 0
        while j <= i:
            print(chr(start),end = '')
            start += 1
            if start > 90:
                start = 65
            j += 1
        print("")
def main():
    try:
        noftri = int(input())
    except ValueError:
        print("Bro r u serious, give a number")
    try:
        values = input()
        lint = values.split(" ")
    except TypeError:
        print("Number of arguments not matched")
    for x in range(noftri):
        triangle(int(lint[x]))

if __name__ == "__main__":
    main()
