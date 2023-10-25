
def encode(password_string):
    password = ""
    for i in password_string:
        password_int = int(i)
        password_int += 3
        if password_int >= 10:
            password_int -= 10
        password += str(password_int)
    return password



def menu():
    password = True
    while password:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            encoded_password = encode(password)
        if menu_option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        if menu_option == 3:
            password = False

def main():
    menu()



if __name__ == "__main__":              #runs the function
    main()
