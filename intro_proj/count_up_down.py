
global numbers
numbers =[]


def array(num):
    global numbers 
    for i in range(100):
        num = num -1
        numbers.append(str(num))
    for i in range(100):
        num = num + 1
        numbers.append(str(num))

def printarray(array):
    count = 0
    for i in range(10):
        print("[", end= ' ')
        for i in range(20):
            print(array[count]+",", end = ' ')
            count = count + 1
        print("]")
    

def main ():

    usernum = int(input("Enter a number Please to be arrayed: "))
    array(usernum)
    printarray(numbers)

main()

    

        