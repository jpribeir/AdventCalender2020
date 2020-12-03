with open("password_database.txt","r") as password_database:
    password_list = []
    for line in password_database.readlines():
        password_list.append(line)