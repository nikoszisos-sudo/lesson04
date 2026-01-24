x = int(input("Δώσε τον πρώτο ακέραιο: "))
y = int(input("Δώσε τον δεύτερο ακέραιο: "))
z = int(input("Δώσε τον τρίτο ακέραιο: "))
lista = [x,y,z]
max_lista = lista[0]
if lista[1] > max_lista:
    max_lista = lista[1]
if lista[2] > max_lista:
    max_lista = lista[2]
print (max_lista)
