class Account:
        def __init__(person,name):
                person.name = name
                person.balance = 0
                person.historylist = []
                person.history('Info',person.balance)

        def deposit(person, cash):
                person.balance += cash
                person.history('Deposit',person.balance)

        def withdraw(person, cash):
                person.balance -= cash
                person.history('Withdraw',person.balance)

        def history(person,type,cash):
            person.historylist.append({
                "amount": cash,
                "balance_after": person.balance, 
                "type": type 
            })
        
        def get_history(person):
            return person.historylist
        

        def __str__(person):
            return f"Account owner: {person.name}, Balance: {person.balance}"
        
if __name__ == "__main__":
    account = Account('Joe Peach')
    account.deposit(222)
    account.withdraw(111)
    print(account)
    print("History:")
    for transaction in account.get_history():
        print(transaction)


