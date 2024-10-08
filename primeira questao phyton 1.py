numero = int(input("Digite um número entre 1 e 10: "))

# verificação de número pelo while com o for complementando
while numero < 1 or numero > 10:
    print("Número inválido! digite um número entre 1 e 10")
    numero = int(input("Digite um número entre 1 e 10 para ver a tabuada:"))

# for para limitar os numeros multiplicados pelo i
print(f"\nTabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")