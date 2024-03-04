cart = {
    'eggs': 6,
    'bread': 2,
}

def show():
    if len(cart) == 0:
        print('Your cart is empty')
    print(cart)
    for k, v in cart.items():
        print(f'There are {v} {k} in your cart')

def add():
    item = input('What item do you want to add?')
    quantity = input('How many do you want to buy?')
    cart[item] = int(quantity)
    print(f'You now have {quantity} {item} in your cart')

def delete():
    item = input('What item do you want to remove?')
    if item in cart:
        del cart[item]
        print(f'{item} has been removed from your cart')
    else:
        print(f'{item} is not in your cart')

def clear():
    global cart
    cart = {}
    print('Your cart is now empty')

def runner():
    while True:
        menu = input('What do you want to do? Show/Add/Delete/Clear/Quit')
        if menu.lower() == 'show':
            show()
        elif menu.lower() == 'add':
            add()
        elif menu.lower() == 'delete':
            delete()
        elif menu.lower() == 'clear':
            clear()
        elif menu.lower() == 'quit':
            return
        else:
            print('Not a valid option')