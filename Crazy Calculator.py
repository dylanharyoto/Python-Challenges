first_input = input("Please input four operator buttons >> ")
second_input = input("Please input the expressions to be calculated >> ")
def crazy_calculator(first, second):
    first = first.split(" ")
    second = second.split(" ")
    result = int(second[0]) # 1
    for i in range(1, len(second), 2):
        if second[i] == "+":
            second[i] = first[0]
        elif second[i] == "-":
            second[i] = first[1]
        elif second[i] == "*":
            second[i] = first[2]
        else:
            second[i] = first[3]
    for j in range(2, len(second), 2):
        if second[j - 1] == "+":
            result += int(second[j])
        elif second[j - 1] == "-":
            result -= int(second[j])
        elif second[j - 1] == "*":
            result *= int(second[j])
        else:
            if int(second[j]) == 0:
                return "division by zero"
            result //= int(second[j])
    return result
final = crazy_calculator(first_input, second_input)
print(final)
