import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

string = lower + upper + numbers + symbols
length = int(input("Letters count:\n"))

password = "".join(random.sample(string,length))

print("The password is:\n",password)

