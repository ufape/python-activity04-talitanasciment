def divisao(x,y):
    if x > y:
            x, y = y, x
    
    numeros = []
    for i in range(x+1, y):
        if i % 5 == 2 or i % 5 == 3:
            numeros.append(i)
            
    return numeros

if __name__ == '__main__':
    d = divisao(7, 10)
    print(d)