# -*- coding: utf-8 -*-
"""EstagioDesenvolvimentoPython_JoseVitor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DcuHqUBSafzMu8SXElqdsZWcB6NRVidr
"""

import unicodedata

def verify_palindromo(texto):
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(char for char in texto if unicodedata.category(char) != 'Mn')
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

frase = input("Digite a frase a ser verificada: ")
if verify_palindromo(frase):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")