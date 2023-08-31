def primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def teste():
    n = int(input("Digite quantos testes realizará: "))
    for i in range(1, n+1):
        x = int(input("Teste {}: ".format(i)))
        if primo(x):
            print("{} é primo.".format(x))
        else:
            print("{} não é primo.".format(x))


if __name__ == '__main__':
    print()
