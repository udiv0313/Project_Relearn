# pretty priting the morning and evening items.
  
# Showing Inventory for morning and evening according to the parameter.

def show_inventory(freelancers, antiques, pet_shop, msg ="Morning Iventory"):
    print(f'{msg}')

    printing_dashes()

    department_store = {**freelancers, **antiques, **pet_shop}
    if msg == "Morning Inventory":
        department_store.pop("name")

    for sno, (shop,stock) in enumerate(department_store.items(), start=1):
        print(f'{sno}. {shop} -> {stock} Gp') 
    
    printing_dashes()


# Inventory
def inventory_store(freelancers, antiques, pet_shop, purse):

    cart = {}

    for shop in (freelancers, antiques, pet_shop):
        
        # print(type(shop))
        print(f'Welcome to {shop["name"]}! (type exit to exit store)\n')
        printing_inventory(shop)

        # print("------------------------------------------------------------------\n")
        printing_dashes()

        buy_item = input(f'what do you want to buy: ').lower()

        print("\n")
        
        if buy_item == "exit" or buy_item not in shop:
            continue
        
        cart_total = sum(cart.values()) 
        cart.update({buy_item:shop.pop(buy_item)})
        buy_items = ", ".join(list(cart.keys()))
    
    return display_purchased_items(freelancers, antiques, pet_shop, buy_items , cart_total, purse, msg="Evening Inventory After Buy")



# displaying the inventory
def display_purchased_items(freelancers, antiques, pet_shop, buy_items, cart_total , purse, msg):

    printing_dashes()

    print(f"You have purchased {buy_items} and your total is {cart_total} Gp, You have {purse - cart_total} Gp from 1000 Gp , Have a nice day Mayhem!")

    printing_dashes()

    show_inventory(freelancers, antiques, pet_shop, msg)



# Pretty printing the inventory 
def printing_inventory(shops):
    shops.pop("name")
    for sno, (shop,price) in enumerate(shops.items(), start=1):
            print(f"{sno}. {shop} -> {price} Gp")


def printing_dashes():
    print("------------------------------------------------------------------\n")





def main():
    freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
    antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
    pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

    purse = 1000

    show_inventory(freelancers, antiques, pet_shop, msg="Morning Inventory")
    inventory_store(freelancers, antiques, pet_shop, purse)



main()

