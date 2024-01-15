def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What's it like in {location}")


greet_with("Carlos", "Paraguay")
    

def key_arguments(a,b,c):
    print(f"A tiene el valor de {a}")
    print(f"B tiene el valor de {b}")
    print(f"C tiene el valor de {c}")

#Pasamos los valores utilizando keyword arguments
# Dentro de la llamada definimos que valor tendrá cada parámetro
key_arguments(c=3, a=1, b=2)

