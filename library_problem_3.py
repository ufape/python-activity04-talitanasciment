def soma():
  while True:
    x = int(input("Digite o valor inicial: "))
    if x == 0:
        break
    soma = 0
    if x % 2 == 1:
        x += 1
    for i in range(x, x+10, 2):
        soma += i

if __name__ == '__main__':
    print()