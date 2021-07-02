import random
import string

#ALL_NUMBER='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
ALL_NUMBER=string.ascii_letters + string.digits

def get_authcode(digits):
    authcode = ''
    for i in range(digits):
        authcode += random.choice(ALL_NUMBER)
    return authcode
def gen_200_codes():
    digit = 6
    code=''
    data=[]
    for i in range(200):
        code=get_authcode(digit)
        data.append(code)
    return data
authcode200 = gen_200_codes()
print(authcode200)

