name = input("Please Input your name: ")
def myBoro(name):
    glo2 = input('Select the Amount You want to Borrow ')
    if glo2 == "1":
        print("Dear " + name + ' ,You have sucessfully been credited #100')

    elif glo2 == '2':
        print("Dear " + name + ' ,You have sucessfully been credited #200')

    elif glo2 == '3':
        print("Dear " + name + ' ,You have sucessfully been credited #300')

    elif glo2 == '4':
        print("Dear " + name + ' ,You have sucessfully been credited #400')

    elif glo2 == '5':
        print("Dear " + name + ' ,You have sucessfully been credited #500')

    else:
        print( "Dear " + name + ' ,Sorry try again Later')


glo1 = input('Enter the USSD code ')
if glo1 == '*123#':
    print('Welcome to GloBoro Me \n 1. #100 \n 2. #200 \n 3. #300 \n 4. #400 \n 5. #500')
    myBoro(name)
    
elif glo1 == '*606#':
    print('Welcome to Mtn \n 1. #100 \n 2. #200 \n 3. #300 \n 4. #400 \n 5. #500') 
    myBoro(name)        
elif glo1 == '*555#':
    print('Welcome to Airtel \n 1. #100 \n 2. #200 \n 3. #300 \n 4. #400 \n 5. #500')
    myBoro(name)      
elif glo1 == '*665#':
    print('Welcome to 9Mobile \n 1. #100 \n 2. #200 \n 3. #300 \n 4. #400 \n 5. #500') 
    myBoro(name)

else:
    print('Invalid code')    