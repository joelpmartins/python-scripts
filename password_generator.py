import random

numeros = "0123456789"
simbolos = "[](){}*@#%&,.;:+-_/!?"
letras = "abcdefghijklmnopqrstuvwxyz"

tamanho = input("Informe o tamanho da senha: ")
tamanho = int(tamanho)

senha = "".join(random.sample(letras + letras.upper() + numeros + simbolos, tamanho))
print(senha)
