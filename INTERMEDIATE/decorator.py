#decorator concept applied , to be studied

def verify_pin(func):
    def wrapper(pin, amount):
        if pin == 1234:
            return func(pin, amount)
        else:
            print("Incorrect PIN! Access denied")

    return wrapper


@verify_pin
def withdraw(pin, amount):
    print(f"{amount} withdrawn successfully!")


withdraw(1234, 500)
withdraw(1111, 10000)
