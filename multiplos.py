"""
Curso: Programação em Python Essencial - Sessão 07.
Aluno: Matheus Martins.
Exercício numero 18 - Encontrando números múltiplos de um número x dentro de um intervalo estabelecido pelo usuário. 
Data: 10/07/2021
"""

# Apresentação:
print('Programa para verificar quantos números múltiplos de um número n existem dentro de um intervalo. \n')

# Declaração de variáveis e listas e entradas de dados.
vetor = []
multiplos = []
numero = int(input('Entre com o valor de consulta: '))
inicio = int(input('Entre com o começo do intervalo: '))
fim = int(input('Entre com o final do intervalo: '))
passo = int(input('Entre com o passo do intervalo: '))

# Verificando se os números são válidos:

if numero and passo != 0:

    # Processamento de informações:
    for x in range(inicio, fim+1, passo):
        vetor.append(x)

    for x in vetor:
        if x % numero == 0:
            multiplos.append(x)

    # Saída de dados:
    print(f'Os números múltiplos de {numero} dentro do intervalo de {inicio} a {fim} ao passo {passo} são: {multiplos}.')
    print(f'Total de números múltiplos: {len(multiplos)} \n')
    print('Obrigado por utilizar meu programa!')

elif numero == 0:
    print('O número de consulta não pode ser 0 (zero)')

elif passo == 0:
    print('O número de passo não pode ser 0 (zero)')

else:
    print('Algo deu errado no programa. Pedimos desculpas.')
