x = int(input("Δώσε τον πρώτο ακέραιο: "))
y = int(input("Δώσε τον δεύτερο ακέραιο: "))
z = int(input("Δώσε τον τρίτο ακέραιο: "))
max_list = [x,y,z]
if x>=y and x>=z:
    print (max_list[0])
elif y>=x and y>=z:
    print (max_list[1])
else:
    print (max_list[2])