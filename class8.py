"""login authentication, define a function to check the supplied username and password is correct.
if correct should print login successfully
if not should print invalid credentials
def login(username,password):
    if username=="admin" and password=="password123":
        print("Login successfully")
    else:
        print("Invalid credentials")
username=input("Enter username: ")
password=input("Enter password: ")
login(username,password) """

'''electricity bill calculation
units less than 100 bill unit *5
<200= till 100 unit *5 + remaining unit *8
>200=100*5 ,200*8 + remaining unit *10
display total bill amount
def calculation(unit):
    if unit < 100:
        total = unit * 5

    elif unit <= 200:
        total = (100 * 5) + (unit - 100) * 8

    else:
        total = (100 * 5) + (100 * 8) + (unit - 200) * 10

    print("Total bill =", total)    `


units = int(input("Enter units: "))
calculation(units) '''
 #otp random
 


