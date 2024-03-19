import streamlit as st
def checkPassword(password):
    upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
    length = len(password)

    if (length < 6):
        print("Password must be at least 6 characters long!\n")
    else:
        for i in range(0, length):
            if (password[i].isupper()):
                upperChars =True
            elif (password[i].islower()):
                lowerChars =True
            elif (password[i].isdigit()):
                digits =True
            else:
                specialChars =True

    if (upperChars == True and lowerChars == True and digits ==True and specialChars == True):
        if (length >= 7):
            return "The strength of password is strong.\n"
        else:
            print("The strength of password is medium.Need more length\n")
    else:
        if (upperChars == True and lowerChars == False and digits ==False and specialChars == False):
            return "Password must contain at least one lower,special character and digit !\nToo Poor password\n"

        elif (upperChars == False and lowerChars == True and digits ==False and specialChars == True):
            return "Password must contain at least one uppercase character and digit !\nIntermediate password\n"

        elif (upperChars == True and lowerChars == True and digits ==False and specialChars == False):
            return "Password must contain at least one special character and digit !\nPoor password\n"

        elif (upperChars == True and lowerChars == False and digits ==True and specialChars == False):
            return "Password must contain at least one lowercase character and digit !\nIntermediate password\n"

        elif (upperChars == False and lowerChars == False and digits ==True and specialChars == True):
            return "Password must contain at least lower and upper case characters!\nMedium password\n"

        elif (upperChars == True and lowerChars == True and digits ==True and specialChars == False):
            return "Password must contain at least one special character !\nIntermediate password\n"
        else:
            return "Medium password"


# password = input("Please enter password: ")


#GUI

st.title("Password Strength Checker")
password = st.text_input("Enter Password ")
if st.button('Check'):
    result=(checkPassword(password))
    st.write(result)