# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

numero = int(input("Digite um número: "))
fatorial = 1  

for cont in range(1, numero + 1):  # O loop deve ir de 1 até o número
    fatorial *= cont 

print(f"O fatorial de {numero} é {fatorial}")
