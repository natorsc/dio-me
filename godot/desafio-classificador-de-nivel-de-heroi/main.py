# -*- coding: utf-8 -*-
'''# Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de 
um herói, depois utilize uma estrutura de decisão para apresentar alguma das 
mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
'O Herói de nome {nome}** está no nível de {nivel}.
'''

GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

# Tratamento de erro para garantir que o nome do herói não esteja vazio.
while True:
    nome_do_heroi = input('Digite o nome do herói: ').strip()
    if nome_do_heroi:
        break
    print('Entrada inválida ou vazia. Por favor, digite o nome do herói.')


# Tratamento de erro para garantir que a XP seja um número válido.
while True:
    entrada = input('Digite a quantidade de XP do herói: ').strip()
    try:
        xp_do_heroi = int(entrada)
        if xp_do_heroi < 0:
            print('O XP não pode ser negativo. Tente novamente.')
        else:
            break
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro válido.')

# 2. Variável para armazenar o nível do herói (inicialmente vazia).
nivel_do_heroi = ''

# Estrutura de decisão para determinar o nível.
if xp_do_heroi <= 1000:
    nivel_do_heroi = 'Ferro'
elif xp_do_heroi <= 2000:
    nivel_do_heroi = 'Bronze'
elif xp_do_heroi <= 5000:
    nivel_do_heroi = 'Prata'
elif xp_do_heroi <= 7000:
    nivel_do_heroi = 'Ouro'
elif xp_do_heroi <= 8000:
    nivel_do_heroi = 'Platina'
elif xp_do_heroi <= 9000:
    nivel_do_heroi = 'Ascendente'
elif xp_do_heroi <= 10000:
    nivel_do_heroi = 'Imortal'
else:
    nivel_do_heroi = 'Radiante'

# 4. Saída final: Exibindo a mensagem.
print(
    f'O Herói de nome {YELLOW}{nome_do_heroi}{RESET} está no nível de '
    f'{GREEN}{nivel_do_heroi}{RESET}.'
)
