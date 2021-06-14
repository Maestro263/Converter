# Convert miles to kilometers
from time import sleep

# Miles to KM
miles = 1.60934
km = 1

# Pounds to KG
pounds = 2.204
kg = 1


def convert_miles():
    convert = int(input("How many km do you want to convert?: "))
    km_converted = convert * miles
    print(km_converted)


def convert_kilos():
    convert = int(input("How many kilograms do you want to convert?: "))
    kg_converted = convert * pounds
    print(kg_converted)


while True:
    start = input('''What would you like to convert, choose a number from the list below:
        1. Km to Miles?
        2. Kg to Pounds
        ''')
    if start == str(1):
        convert_miles()
        sleep(2)
    elif start == str(2):
        convert_kilos()
        sleep(2)
    else:
        print("There was an error, wait a second and try again")
        sleep(2)
