import random


symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_lens = int(input('Введите длинну пароля'))
r_password = ''

for i in range(pass_lens):
    r_password += random.choice(symbols)

print(r_password)
