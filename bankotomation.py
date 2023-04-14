johnaccount={
    "name":"John Wick",
    "bankaccount":4000,
    "additionalaccount":2000
}

lenaaccount={
    "name":"John Wick",
    "bankaccount":4000,
    "additionalaccount":2000
}

def paracek(account,cash):
    print(f"Hello {account['name']}")
    if account["bankaccount"]>=cash:
        account["bankaccount"]-=cash
        print("You can take your money.")
        print("balance is : "+str(account["bankaccount"])+" at the moment.")
    else:
        totalmoney=account["bankaccount"]+account["additionalaccount"]
        if totalmoney>=cash:
            additionalaccountuse=input("Do you want use additional account?")
            if additionalaccountuse=="e":
                account["additionalaccount"]-=cash
                print("You can take your money.")
                print("Balance in additional account is : "+str(account["additionalaccount"]))
                
            else:
                print(f"There is {account['bankaccount']} $ in {account['name']} account.")
        else:
            print("Balance is not enough.")
# paracek(johnaccount,2000)
# paracek(johnaccount,6000)
# paracek(johnaccount,7000)
paracek(johnaccount,3000)
paracek(johnaccount,2000)

# Don't forget!You must remove above codes from comment row.