accounts = {}

def my_account() :
    host = input("Please enter your Username : ")
    while host in accounts:
        if host in accounts:
            pass_key = input(f"{host} Please enter your Password : ")
    
            if accounts[host] == pass_key:
                print("You've entered the secret chambers of programing")
                break
    
            else:
                print(f"{host} has entered the wrong password please try again.")
                continue
        else:
            print(f"{host} was not found please try agin or create an account.")
            return no_account()

def no_account() :
    username = input("Enter a Username : ")
    if username in accounts:
        print(f"{username} already exist please try agian.")
        
    else: 
        passwords = input("Enter a Password : ")
        accounts[username] = passwords
        print(f"Thanks for signing up {username}")

# take user input / choice and lower case it for comparison below
user = input("Have you made an account before? please type YES/NO : ").lower() 
if user == "yes" :
    my_account()  

else: 
    no_account()
    my_account()

    





