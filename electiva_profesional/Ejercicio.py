#1
name = "Yenifer"
age = 20
favouriteFood = "arroz con huevo"
text = f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi comida favorita es {favouriteFood}"
print(text)

#2
FullName = "Yenifer Lopez"
lengthUsuario = len(FullName.strip())
print(f"Hola, {FullName}! Tu nombre tienen {lengthUsuario} letras, excluyendo los espacios")

#3
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
print( f"Las ventas de la empresa lactea aumentaron un {round(increaseSalesPercent,2)}% y los ingresos crecieron un {round(revenueGrowthPercent,2)}%")

#4
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"

modifiedMessange = secretMessage[3:]
decodedMessage = modifiedMessange[::2]
print(decodedMessage)


#5
text1 = "El nombre 'Python' viene dado por la aficion de Van Rossum al grupo Monty Python"
palabra = text1.split()
numeroo_palabras = len(palabra)
print(f"Numero de palabras de la frase: {numeroo_palabras}")

#6
word = "camila"
cambiarletra =word.replace('a','e')
print(cambiarletra)

#7
sentence = "la historia del lenguaje de programación Python"
palabraas = sentence.split()
inversa = palabraas[::-1]
sentence_invertir = " ".join(inversa)
print(sentence_invertir)