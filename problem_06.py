# -*- coding: utf-8 -*-

# Jamerson Lucas Tenorio 
# UAG00098
# Problem Set 1 - Problem 6
# Description:


"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
O arquivo de entrada contém três valores inteiros.
7 14 106

Processes:
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

maiorAB = (a + b + abs(a - b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Output(s):
Imprima conforme exemplo a seguir.
Exemplo:
O maior número é: 106
"""


def main():
  
    a = int(input("Digite o valor A: "))
    b = int(input("Digite o valor B: "))
    c = int(input("Digite o valor C: "))


    maiorAB = (a + b + abs(a - b)) // 2


    maior_numero = (maiorAB + c + abs(maiorAB - c)) // 2 
    print(f"O maior número é: {maior_numero}")

if __name__ == '__main__':
    main()
