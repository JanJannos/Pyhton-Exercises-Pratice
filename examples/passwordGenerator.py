import string
import random


def gen():
    s1 = string.ascii_uppercase    
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    passwordLength = int(input("Enter the Length of the Password ?"))
    result = []
    result.extend(s1)
    result.extend(s2)
    result.extend(s3)
    result.extend(s4)

    random.shuffle(result)
    password = ("".join(result[0:passwordLength]))

    print(password)

gen()
