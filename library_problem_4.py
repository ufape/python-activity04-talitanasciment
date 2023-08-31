def e_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n
def testar_numeros_perfeitos():
    n = int(input("Digite quantos testes realizará: "))
    for i in range(1, n+1):
        x = int(input(f"Teste {i}: "))
        if e_perfeito(x):
            print(f"{x} é perfeito.")
        else:
            print(f"{x} não é perfeito")

if __name__ == '__main__':
    print()