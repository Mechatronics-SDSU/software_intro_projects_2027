def main():
    number = int(input("Enter a starting number: "))
    arr = []

    for i in range(10):
        arr.append([])
        for j in range(20):
            arr[i].append(number)
            if i > 4:
                number -= 1
            else:
                number += 1
        print(arr[i])


if __name__ == "__main__":
    main()
