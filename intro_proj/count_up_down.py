def create_array(starting_value):
    rows = 10
    columns = 20
    halfway = (rows * columns) // 2

    array = []
    value = starting_value

    for i in range(rows):
        current_row = []

        for j in range(columns):
            position = i * columns + j

            current_row.append(value)

            if position < halfway:
                value += 1
            else:
                value -= 1

        array.append(current_row)

    return array


def main():
    starting_value = int(input("Enter a starting number: "))

    array = create_array(starting_value)

    for row in array:
        print(*row)


if __name__ == "__main__":
    main()
    