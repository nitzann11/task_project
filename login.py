while True:
    menu=print("""
    Login menu:
    1.Log in
    2.Create a new account
    3.change password
    4.exit""")

    options=["1","2","3","4"]
    action=input("choose option:1-4")
    while action not in options:
        if action in options:
            if action=="1":
                pass
            elif action =="2":
                pass
            elif action =="3":
                pass
            elif action=="4":
                pass
        else:
            print("invalid action, try again..")
