try:
    age = int(input("How old are you: "))
    if age > 18 and age <= 99:
        print("You are welcome for a drink!")
    elif age > 99:
        print("Are you sure you want the drink?")
    else:
        print("You are too young!")
except:
    print("The answer must be an integer!")

a = [1,2,3,6,7,8]
# for
for number in a:
    if 9 == number:
        print("The number was found!")
        break
else:
    print("The number is not found!")

from time import sleep
# while
i = 0
while True:
    print(f"Number: {i}")
    sleep(0.1)
    i += 1
    # i = i + 1
    if i > 50:
        break



