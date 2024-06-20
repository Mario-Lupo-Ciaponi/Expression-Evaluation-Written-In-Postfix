"""
Expression
Evaluation
"""


def is_whole_number(number):
    """
    Sees if the number is whole or not.
    """
    return number.is_integer()


def is_zero(number):
    return number == 0


def sum_operation(stack_of_numbers):
    """
    Sums two numbers. Then, the sum is added to the stack.
    """

    first_number, second_number = stack_of_numbers.pop(-2), stack_of_numbers.pop(-1)

    result = first_number + second_number

    stack_of_numbers.append(result)

    return stack_of_numbers


def difference_operation(stack_of_numbers):
    """
    Subtracts two numbers. Then, the difference is added to the stack.
    """

    first_number, second_number = stack_of_numbers.pop(-2), stack_of_numbers.pop(-1)

    result = first_number - second_number

    stack_of_numbers.append(result)

    return stack_of_numbers


def multiplication_operation(stack_of_numbers):
    """
    Multiplicates two numbers. Then the product is added to the stack.
    """

    first_number, second_number = stack_of_numbers.pop(-2), stack_of_numbers.pop(-1)

    result = first_number * second_number

    stack_of_numbers.append(result)

    return stack_of_numbers


def division_operation(stack_of_numbers):
    """
    Divides two numbers. Then the division is added to the stack.
    """

    first_number, second_number = stack_of_numbers.pop(-2), stack_of_numbers.pop(-1)

    if is_zero(second_number):
        print("Cannot divide by zero!")

        return stack_of_numbers, False

    # If it is not zero, it will do the division

    result = first_number / second_number

    if is_whole_number(result):
        result = int(result)

    stack_of_numbers.append(result)

    return stack_of_numbers, True


def postfix_expression_evaluation_result(expression):
    stack_of_numbers = []
    is_valid = True

    if expression[-1].isdigit() or expression[-1] == "-" and len(expression[-1]) > 1 \
            or expression[0] == "+" or expression[0] == "-" or expression[0] == "*" or expression[0] == "/" \
            or expression[1] == "+" or expression[1] == "-" or expression[1] == "*" or expression[1] == "/":
        print("The postfix expression is not valid!")
        is_valid = False

    if is_valid:
        for element in expression:
            if element.isdigit() or element[0] == "-" and len(element) > 1:
                stack_of_numbers.append(int(element))
            else:
                if element == "+":
                    stack_of_numbers = sum_operation(stack_of_numbers)
                elif element == "-":
                    stack_of_numbers = difference_operation(stack_of_numbers)
                elif element == "*":
                    stack_of_numbers = multiplication_operation(stack_of_numbers)
                elif element == "/":
                    stack_of_numbers, is_valid = division_operation(stack_of_numbers)

                    if not is_valid:
                        break
                else:
                    print("Invalid operation!")
                    is_valid = False
                    break

    return stack_of_numbers, is_valid


def main():
    expression = input("Type the postfix expression(e.g. '5 6 2 + *' infix: '5 * (6 + 2)'): ").split()

    stack_of_numbers, is_valid = postfix_expression_evaluation_result(expression)

    if is_valid:
        result = stack_of_numbers[0]

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
