ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


start = 0
passes = []
dict = 0
dict_check = 0
level_counter = 0
level_under_check = 0
level_upper_check = 0
level_punct_check = 0
level_number_ckeck = 0

def open_dict(x):
    text = open(x, 'r+')
    for line in text.readlines():
        if len(line) >= 8:
            passes.append(line[:-2])
    print("Dict added to passes list successfully")
    print("input exit to get out")
    text.close()


def is_upper(x):
    for i in password:
        if i in ascii_uppercase:
            return True

def is_under(x):
    for i in password:
        if i in ascii_lowercase:
            return True

def is_punct(x):
    for i in password:
        if i in punctuation:
            return True


choose = input(str("Do you want to add dict? y/n "))
if choose == 'y':
    source = input(str("Put dictionary in same folder as .py file and input text name with .format here: "))
    dict = 1
    open_dict(source)
    start += 1
if choose == 'n':
    print("Working without Dictionary")
    print("input exit to get out")
    dict = 2
    start += 1

while start == 1:
    password = input(str("Input password: "))
    if password == 'exit':
        start = 0
        break

    # checking if password under 8 charts
    if len(password) < 8:
        print("Password has less then 8 symbols")

    # checking if password is 8 charts
    if len(password) == 8:
        level_counter += 1
        if dict == 1:
            if password in passes:
                dict_check = 1
                print("Password was found in dictionary, the password is weak")
        if is_under(password):
            level_under_check += 1
        if is_upper(password):
            level_upper_check += 1
        if is_punct(password):
            level_punct_check += 1
        for i in range(10):
            if str(i) in str(password):
                level_number_ckeck += 1

    # checking if password is 9 or 10 charts
    if len(password) == 9 or len(password) == 10:
        level_counter += 2
        if dict == 1:
            if password in passes:
                dict_check = 1
                print("Password was found in dictionary, the password is weak")
        if is_under(password):
            level_under_check += 1
        if is_upper(password):
            level_upper_check += 1
        if is_punct(password):
            level_punct_check += 1
        for i in range(10):
            if str(i) in str(password):
                level_number_ckeck += 1

    # ckecking if password is  10 or 11 charts

    if len(password) == 11 or len(password) == 12:
        level_counter += 3
        if dict == 1:
            if password in passes:
                dict_check = 1
                print("Password was found in dictionary, the password is weak")
        if is_under(password):
            level_under_check += 1
        if is_upper(password):
            level_upper_check += 1
        if is_punct(password):
            level_punct_check += 1
        for i in range(10):
            if str(i) in str(password):
                level_number_ckeck += 1

    # checking if password is more then 12 charts

    if len(password) > 12:
        level_counter += 4
        if dict == 1:
            if password in passes:
                dict_check = 1
                print("Password was found in dictionary, the password is weak")
        if is_under(password):
            level_under_check += 1
        if is_upper(password):
            level_upper_check += 1
        if is_punct(password):
            level_punct_check += 1
        for i in range(10):
            if str(i) in str(password):
                level_number_ckeck += 1



    if level_counter == 1:
        if dict_check == 0:
            if level_under_check == 0:
                print("password has no letters, password is weak")
            else:
                print("Password has only 8 charts")
                if level_number_ckeck >= 1:
                    print("The password has numbers")
                    if level_upper_check == 1:
                        print("The password has Uppercase")
                        if level_punct_check == 1:
                            print("The password has punctuation")
                        else:
                            print("Password is strong")
                    else:
                        print("Password is middle")
                else:
                    print("password is weak")



    if level_counter == 2:
        if dict_check == 0:
            if level_under_check == 0:
                print("password has no letters, password is weak")
            else:
                print("Password has 9 to 10 charts")
                if level_number_ckeck >= 1:
                    print("The password has numbers")
                    if level_upper_check == 1:
                        print("The password has Uppercase")
                        if level_punct_check == 1:
                            print("The password has punctuation")
                            print("The password is very strong")
                        else:
                            print("Password is strong")
                    else:
                        print("Password is middle")
                else:
                    print("password is weak")


    if level_counter == 3:
        if dict_check == 0:
            if level_under_check == 0:
                print("password has no letters, password is weak")
            else:
                print("Password has 11 to 12 charts")
                if level_number_ckeck >= 1:
                    print("The password has numbers")
                    if level_upper_check == 1:
                        print("The password has Uppercase")
                        if level_punct_check == 1:
                            print("The password has punctuation")
                            print("The password is very strong")
                        else:
                            print("Password is strong")
                    else:
                        print("Password is strong")
                else:
                    print("password is middle")

    if level_counter == 4:
        if dict_check == 0:
            if level_under_check == 0:
                print("password has no letters, password is weak")
            else:
                print("Password has 11 to 12 charts")
                if level_number_ckeck >= 1:
                    print("The password has numbers")
                    if level_upper_check == 1:
                        print("The password has Uppercase")
                        if level_punct_check == 1:
                            print("The password has punctuation")
                            print("The password is very strong")
                        else:
                            print("Password is very strong")
                    else:
                        print("Password is very strong")
                else:
                    print("password is strong")