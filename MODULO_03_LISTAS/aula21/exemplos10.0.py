def fatorial(num):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
        

n = int(input('Digite um número, para vrf o seu FATORIAL: '))
print(f'O fatorial {n} é {fatorial(n)}')
