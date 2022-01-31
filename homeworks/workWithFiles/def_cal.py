def calc_add(first, second):
    return first + second


def calc_ded(first, second):
    return first - second

def data_entry():
    first = int(input("Please write first argument: "))
    operator = input("Please choose operator: ")
    second = int(input("Please write second argument: "))
    operations = {"+": calc_add(first, second), "-": calc_ded(first, second)}
    if operator in operations:
        with open("reslts.txt", "w") as file:
            file.write(f"{first} {operator} {second} = {operations[operator]}")
        print("Results saved in file 'reslts.txt'")
    else:
        print("An error has occurred, please contact support")



