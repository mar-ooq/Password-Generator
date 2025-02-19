import string
import random
lowercase_letters_list = list(string.ascii_lowercase)
uppercase_letters_list = list(string.ascii_uppercase)
special_characters_list = list(string.punctuation)
digits_list = list(string.digits)
password = ''

length = int(input("Enter the length of your password:"))
#special characters
question = input("Should the password contain any special characters?")
while question not in ['yes', 'no', 'Yes', 'No', 'YES', 'NO']: 
    print("Invalid input. Please enter 'yes' or 'no'.")
    question = input("Should the password contain any special characters?")

contain_special_characters = True if question in ['yes', 'YES', 'Yes'] else False

#upper letters
question = input("Should your password contain upper letters?")
while question not in ['yes', 'no', 'Yes', 'No', 'YES', 'NO']: 
    print("Invalid input. Please enter 'yes' or 'no'.")
    question = input("Should the password contain any special characters?")

contain_upper_letters = True if question in ['yes', 'YES', 'Yes'] else False

#digits

question = input("Should your password contain digits?")
while question not in ['yes', 'no', 'Yes', 'No', 'YES', 'NO']: 
    print("Invalid input. Please enter 'yes' or 'no'.")
    question = input("Should the password contain any special characters?")

contain_digits = True if question in ['yes', 'YES', 'Yes'] else False

#randoms
x=0

if contain_special_characters and contain_special_characters and contain_digits:
    while x<length:
        main_random = random.randint(1,4)
        match main_random:
            case 1:
                lowercase_random = random.choice(lowercase_letters_list)
                password += lowercase_random
            case 2:
                uppercase_random = random.choice(uppercase_letters_list)
                password += uppercase_random
            case 3:
                special_character_random = random.choice(special_characters_list)
                password += special_character_random
            case 4:
                digit_random = random.choice(digits_list)
                password += digit_random
        x += 1
elif contain_special_characters and contain_upper_letters and not contain_digits:
    while x<length:
        main_random = random.randint(1,3)
        match main_random:
            case 1:
                lowercase_random = random.choice(lowercase_letters_list)
                password += lowercase_random
            case 2:
                uppercase_random = random.choice(uppercase_letters_list)
                password += uppercase_random
            case 3:
                special_character_random = random.choice(special_characters_list)
                password += special_character_random
        x += 1
elif contain_special_characters and contain_digits and not contain_upper_letters:
    while x<length:
        main_random = random.randint(1,3)
        match main_random:
            case 1:
                lowercase_random = random.choice(lowercase_letters_list)
                password += lowercase_random
            case 2:
                digit_random = random.choice(digits_list)
                password += digit_random
            case 3:
                special_character_random = random.choice(special_characters_list)
                password += special_character_random
        x += 1
elif contain_digits and contain_upper_letters and not contain_special_characters:
    while x<length:
        main_random = random.randint(1,3)
        match main_random:
            case 1:
                lowercase_random = random.choice(lowercase_letters_list)
                password += lowercase_random
            case 2:
                uppercase_random = random.choice(uppercase_letters_list)
                password += uppercase_random
            case 3:
                digit_random = random.choice(digits_list)
                password += digit_random
        x += 1
elif contain_special_characters and not contain_upper_letters and not contain_digits:
    while x<length:
        main_random = random.randint(1,2)
        match main_random:
            case 1:
                lowercase_random = random.choice(lowercase_letters_list)
                password += lowercase_random
            case 2:
                special_character_random = random.choice(special_characters_list)
                password += special_character_random
        x += 1
elif contain_upper_letters and not contain_digits and not contain_special_characters:
    while x<length:
        main_random = random.randint(1,2)
        match main_random:
            case 1:
                lowercase_random = random.choice(lowercase_letters_list)
                password += lowercase_random
            case 2:
                uppercase_random = random.choice(uppercase_letters_list)
                password += uppercase_random
        x += 1
elif contain_digits and not contain_special_characters and not contain_upper_letters:
    while x<length:
        main_random = random.randint(1,2)
        match main_random:
            case 1:
                lowercase_random = random.choice(lowercase_letters_list)
                password += lowercase_random
            case 2:
                digit_random = random.choice(digits_list)
                password += digit_random
        x += 1
else:
    while x<length:
        lowercase_random = random.choice(lowercase_letters_list)
        password += lowercase_random
        x += 1
print(password)