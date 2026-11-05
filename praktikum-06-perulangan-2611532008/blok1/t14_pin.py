pin = input ("Enter PIN:    ") #E
correct_pin = "1234" #K
MAX_ATTEMPTS = 3 #H
attempts = 1 #B
while pin != correct_pin and attempts < MAX_ATTEMPTS: #C
    print ("Inccorect PIN.") #I
    pin = input ("Enter PIN:    ") #E
    attempts += 1 #G
if pin == correct_pin: #J
    print ("Access granted.") #D
else: #F
    print("Account locked.") #A
 
