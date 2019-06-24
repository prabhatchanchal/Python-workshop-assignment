cart = []
new_cart=[]
choice = "yes"
while choice == "yes":
    item = input("Add Food Item in Your Cart: ")
    cart.append(item)
    choice = input("Would you like to add more items(yes/no): ")
while cart:
    minimum = cart[0]  # arbitrary number in list 
    for x in cart: 
        if x < minimum:
            minimum = x
    new_cart.append(minimum)
    cart.remove(minimum)    
for elm in new_cart:
    print(elm)
