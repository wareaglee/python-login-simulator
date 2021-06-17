accounts = {}
def mAccount() :
    Host = input("Please enter your Username : ")
    while Host in accounts:
        if Host in accounts:
            pass_key = input(f"{Host} Please enter your Password : ")
    
            if accounts[Host] == pass_key:
                print("You've entered the secret chambers of programing")
    
            else:
                print(f"{Host} has entered the wrong password please try again.")
        else:
            print(f"{Host} was not found please try agin or create an account.")
            return noAccount()
def noAccount() :
    username = input("Enter a Username : ")
    if username in accounts:
        print(f"{username} already exist please try agian.")

    else: 
        passwords = input("Enter a Password : ")
        accounts[username] = passwords
        print(f"Thanks for signing up {username}")

User = input("Have you made an account before? please type YES/NO : ").lower() # take user input / choice and lower case it for comparison below
if User == "yes" :
    mAccount()
    
else: 
    noAccount()
    





