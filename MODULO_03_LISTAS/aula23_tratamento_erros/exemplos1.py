try:
    a = int(input('Digite numerador: '))
    b = int(input('Digite dividendo: '))
    r = a / b
except Exception as erro:
    print(f'Infelizmente ocorreu o seguinte erro... {erro.__class__} :( ')
else:
    print(f'O resultado da divisão é: {r}')
finally:
    print('Volte sempre!')
