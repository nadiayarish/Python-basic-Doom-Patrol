def calc_add(first, second):
    result = first + second
    with open("result.txt", "w") as file:
        file.write(f"{first} + {second} = {result}")


def calc_ded(first, second):
    result = first - second
    with open("result.txt", "w") as file:
        file.write(f"{first} - {second} = {result}")


def data_entry():
    first = int(input("Please write first argument: "))
    operator = input("Please choose operator (+ or -): ")
    second = int(input("Please write second argument: "))
    if operator == "+":
        calc_add(first, second)
    elif operator == "-":
        calc_ded(first, second)
    print("Result saved in file 'Result.txt'")
