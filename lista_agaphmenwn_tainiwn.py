x = input("Δώσε την πρώτη ταινία: ")
y = input("Δώσε την δεύτερη ταινία: ")
z = input("Δώσε τον τρίτη ταινία: ")
my_list = [x,y,z]
w = input("Δώσε την καινούργια ταινία: ")
if w in my_list:
    print("Δεν έγινε αποθήκευση")
else:
    my_list.append(w)
my_list.sort()
print (my_list)
print (len(my_list))
