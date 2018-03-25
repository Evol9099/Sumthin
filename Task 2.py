import random
bullet = 30
securitypresent = 10
panic = 89

def security(securitypresent, bullet):
    dismantled = False
    while securitypresent != 0:
        if random.randint(0,10) > 3:
            bullet -= 1
            securitypresent -= 1
        else: bullet -= 1
    if securitypresent == 0:
        dismantled = True
    return dismantled

def civillian (panic,bullet):
    neutralized = False
    x = 0
    while panic > 10:
        if panic <= 30:
            print("Shut up or I'll shoot!")
            panic -= 20
        if panic <= 60:
            print("Get down, hands behind your head.")
            panic -= 30
        if panic <= 90:
            bullet -= 3
            panic -= 30
    if panic <= 10:
        neutralized = True
    return neutralized

def Rob (demeanor,bullet):
    x = 0
    money = 0
    desired = 0
    print("Empty the cash!")
    while money != desired:
        if demeanor == "submissive":
            money += 5000
        elif demeanor == "stubborn":
            if x == 0
                print("DO IT NOW!")
                x += 1
            elif x == 1
                print("I'll shoot")
            elif x == 2
                bullet -= 2
                money += 20000
                desired = money
                print("RUN!")



