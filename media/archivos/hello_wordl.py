
sol = True
hora = 10
if sol and hora < 12:
    print("Buenos días")
elif sol and hora >= 12:
    print("Buenas tardes")
else:
    print("Buenas noches")

suma = 0
x = 0
while x<10:
    suma +=x
    x+=1
print(x)

repetir = True
while repetir:
    respuesta = input("Desea repetir el ciclo? (Y/n)")
    if respuesta == "Y":
        repetir = True
        print("Repito...")
    elif respuesta == "n":
        repetir = False
        print("Bye")
    else:
        print("Error, valor invalido")

suma=0
for x in range(10):
    suma+=x            
print(suma)

print(list(range(10)))

frutas = ["manzana","per","piñ","guyb","fresa"]
for fruta in frutas:
    [print(fruta) for fruta in frutas if 'a' in fruta]

triangulos = [
    [4,3,10], #base
    [4,10,20] #altura
    ]
area_triangulos = [b*a/2 for a,b in zip(triangulos[0],triangulos[1])]
print(area_triangulos) #[8.0, 15.0, 100.0]

lista1 = [numero**2 for numero in range(0,11)]
print(lista1) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lista = [numero for numero in 
            [numero**2 for numero in range(0,11)]
                if numero % 2 == 0]
print(lista) #[0, 4, 16, 36, 64, 100]

name = "Daniel"
years = 29
print(f'Hola, {name}. Su edad es: {years}')

print(f'la multiplicación de 23 por 5 es {23*5}')

a = 10
b = 20
print(f'a es mayor a b? {a>b}')
print(f'a es menor a b? {a<b}')


deportes = ['Futbol', 'Basquetbol','Volibol', 'Tenis','Beisbol']
print(f'Los deportes entre el index -4 y -1 son {deportes[-4:-1]}')
#Los deportes entre el index -4 y -1 son ['Basquetbol', 'Volibol', 'Tenis']

deportes = ['Futbol', 'Basquetbol','Volibol', 'Tenis','Beisbol']
deportes[:-1] = ["Bascketball","Volleyball","Tenis"]
print(deportes) #['Bascketball', 'Volleyball', 'Tenis', 'Beisbol']

#unpack tuples
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#unir tuplas

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#multiplciar tuplas
tuple2 = tuple1 * 2

#unica manera de acceder a los sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


thisset.add("orange")
thisset.update(tuple3)
print(thisset)

thisset.remove("banana")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

y = x.intersection(y)
x.symmetric_difference_update(y)

z = x.difference(y)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car = dict(brand = "Ford", model = "Mustang", year = 1964)

#accesar 
x = car["model"]
x = car.get("model")
#toma todas las claves de la lista
x = car.keys()
print(x) #dict_keys(['brand', 'model', 'year'])
values = car.values() 
print(values) #dict_values(['Ford', 'Mustang', 1964])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#verificar alguna clave en un diccionario
if "model" in thisdict:
  print("'model' es una de las claves del diccionario")

#cambiar item
car["model"] = "Figo"
car.update({"model":"Figo"})
#eliminar item
car.pop("model")
car.popitem()


for x in range(1,7):
    if x == 4:
        continue
    print(x)

        
#anidado
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily.get('child1').get('name')) #Emil
myfamily["child1"]["name"]="Daniel"
for member in myfamily.items():
    for m in member:
        print(m)


def saludar():
  print("Hello from a function")

saludar()
def saludar2(nombre="Usuario"):
    print(f"Hello from a function {nombre}")

saludar2()

def sumar(a,b):
    return a+b
sumar(4, 4)

sumar = lambda a, b : a + b
print(sumar(2,3))

def saludar_alumno(**alumno):
  print(f"Hola,  {alumno['nombre']}")
  print(f"Tu edad es:  {alumno['edad']}")
  print(f"Tu tipo sanguineo es:  {alumno['tipo_sanguineo']}")

saludar_alumno(nombre="Emil", edad = 12, tipo_sanguineo="O+")


mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrado = filter(lambda x: x % 2 != 0, mi_lista)

print(list(filtrado))
# [1, 3, 5, 7, 9]

class Person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f'Hola, {self.nombre}')

p1 = Person('Daniel',30)
p1.saludar() #imprime 'Hola, Daniel'
p1.nombre = 'Rubén'
p1.saludar() #imprime 'Hola, Rubén'
print(f'Los deportes entre el index -4 y -1 son {deportes[-4:0]}')
deportes = ['Futbol', 'Basquetbol','Volibol', 'Tenis','Beisbol']

deportes[3:] =  ["Bascketball","Volleyball"]
print(deportes) #['Futbol', 'Bascketball', 'Volleyball']





