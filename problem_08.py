

# -*- coding: utf-8 -*-

# Jamerson Lucas Tenorio 
# UAG00098
# Problem Set 1 - Problem 7
# Description:


"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Seis valores, negativos e/ou positivos.
Exemplo:
Valor (1/6): 7
Valor (2/6): -5
Valor (3/6): 6
Valor (4/6): -3.4
Valor (5/6): 4.6
Valor (6/6): 12

Processes:
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Output(s):
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
Exemplo:
Detectamos 4 valores positivos.
"""


def main():
    num1 = float(input(f"Valor (1/6): "))
   
    num2 = float(input(f"Valor (2/6): "))

    num3 = float(input(f"Valor (3/6): "))

    num4 = float(input(f"Valor (4/6): "))

    num5 = float(input(f"Valor (5/6): "))

    num6 = float(input(f"Valor (6/6): "))

    valores_positivos = 0
   
    if num1 > 0:
      valores_positivos = valores_positivos + 1
    if num2 > 0:
      valores_positivos = valores_positivos + 1
    if num3 > 0:
      valores_positivos = valores_positivos + 1
    if num4 > 0: 
      valores_positivos = valores_positivos + 1
    if num5 > 0:
      valores_positivos = valores_positivos + 1
    if num6 > 0:
      valores_positivos = valores_positivos + 1


    print(f"Detectamos {valores_positivos} valores positivos.")
      
if __name__ == '__main__':
    main()
