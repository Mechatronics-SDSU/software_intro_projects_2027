import numpy as np

def create_array(start):
    arr = np.zeros((10, 20), dtype=int)

    value = start

    for i in range(10):
        for j in range(20):

            index = i * 20 + j

            if index < 100:
                arr[i][j] = value
                value += 1
            else:
                arr[i][j] = value
                value -= 1

    return arr

def main():
    start = int(input("Enter a starting number: "))
    arr = create_array(start)
    print(arr)


if __name__ == "__main__":
    main()