# -*- coding: utf-8 -*-
"""condicional3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xRAVBbnDBEL9ClCs8ZopxrATYLITCtZv
"""

#if condição1:
    # faça algo
#elif condição2:
    # faça outra coisa
#elif condição3:
    # faça mais alguma coisa
#else:
    # faça algo diferente

media =float(input('digite a média: '))
if media >= 6.0:
	print('aprovado(a)')
media =float(input('digite a média: '))
if media >= 6.0:
	print('aprovado(a)')
elif 6.0 > media >= 4.0:
    print('recuperação')
else:
    print('reprovado(a)')