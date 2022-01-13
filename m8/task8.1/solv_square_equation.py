
def validate_param():
    print("ax^2 + bx + c = 0\nPlease enter values for the parameters (only integer):")
    attempts = 3
    while attempts > 0:
        try:
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
        except ValueError:
            attempts -= 1
            print(f'\nThe value is not an integer.\nYou only have {attempts} attempt(s).\n')
        else:
            if a == 0:
                print("\nParameter a is 0. This is not a square equation.")
                quit()
            return a, b, c
    if attempts == 0:
        print("You have used all your attempts. Terminating the script...")
        quit()


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def roots(d, a, b, c):
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif d == 0:
        x = -b / (2 * a)
        return round(x, 2), None
    else:
        return None, None


def solv_square(a, b, c) -> roots:
    d = discriminant(a, b, c)
    return roots(d, a, b, c)


def square_print(a, b, c, result):
    print("\nResult:")
    print(f'D = {discriminant(a, b, c)}')
    x1, x2 = result
    if x1 is None and x2 is None:
        print("The equation does not have any root.")
    elif x2 is None:
        print(f'x = {x1}')
    else:
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')


def main():
    parameters = validate_param()
    a = parameters[0]
    b = parameters[1]
    c = parameters[2]
    result = solv_square(a, b, c)
    square_print(a, b, c, result)


if __name__ == "__main__":
    main()
