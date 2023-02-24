import random


def NameAndAge():
    Name = str(input("Ingrese su nombre"))
    Age = int(input("Ingrese su edad"))

    print(f"Hola {Name}, su edad es {Age}")


def Circle(Radius):
    AreaCircle = (Radius * 3.1416) ** 2
    print(AreaCircle)


def RandomNumbers():
    List = []
    for i in range(random.randint(1, 10)):
        List.append(random.randint(1, 10))
    print(List)


def ParOrImpar(Number):
    if Number % 2 == 0:
        print("Es par")
    else:
        print("Es impar")


ParOrImpar(4)


def FarenheitOrCelcius(F):
    C = (F - 32) / 1.8
    print(C)


def SumList(List):
    Sum = 0
    for i in range(len(List)):
        Sum = Sum + List[i]
    print(Sum)


def BigAndSmall(List=list):
    for i in range(len(List)):
        First = List[0]
        if List[i] > First:
            First == List[i]
        else:
            List.remove(i)


def InvertedList(List):
    return List[::-1]


def print_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(i * columns + j + 1)
        matrix.append(row)
    for row in matrix:
        print(row)


rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
print_matrix(rows, columns)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def generate_even_numbers():
    even_numbers = []
    for i in range(2, 101, 2):
        even_numbers.append(i)
    return even_numbers


even_numbers = generate_even_numbers()
print(even_numbers)


def PrintOneToTen():
    for i in range(10):
        print(i)


def NumbersOperations():
    N1 = float(input("Enter first number: "))
    N2 = float(input("Enter second number: "))

    print("Sum: ", N1 + N2)
    print("Difference: ", N1 - N2)
    print("Product: ", N1 * N2)
    print("Quotient: ", N1 / N2)


def Media(Numeros):
    return sum(Numeros) / len(Numeros)


def palindrome(Texto):
    Texto = Texto.lower().replace(" ", "")
    return Texto == Texto[::-1]


user_input = input("Introduzca el texto: ")
if palindrome(user_input):
    print("El texto es un palindromo")
else:
    print("El texto no es un palindromo")