def greet_user():
    print("Hello World!")
    
greet_user()

def greet_user(username):
    print("Hello " + username + ". Welcome to the Website!")
    
greet_user("Klaus Peter")


def calculate_prize(prize, versandart):
    if versandart == "premium":
        prize += 5
    else:
        prize += 1
    return prize


gesamtpreis = calculate_prize(versandart="premium", prize=12)
print(gesamtpreis)