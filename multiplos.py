"""
Curso: Programação em Python Essencial - Sessão 07.
Aluno: Matheus Martins.
Exercício numero 18 - Encontrando números múltiplos de um número x dentro de um intervalo estabelecido pelo usuário. 
Data: 10/07/2021
"""

vetor = []
multiplos = []
numero = int(input('Entre com o valor de consulta: '))
inicio = int(input('Entre com o começo do intervalo: '))
fim = int(input('Entre com o final do intervalo: '))
passo = int(input('Entre com o passo do intervalo: '))

for x in range(inicio, fim, passo):
    vetor.append(x)

for x in vetor:
    if x % numero == 0:
        multiplos.append(x)

print(f'Os números múltiplos de {numero} dentro do intervalo de {inicio} a {fim} ao passo {passo} são: {multiplos}.')
print(f'Total de números múltiplos: {len(multiplos)}')