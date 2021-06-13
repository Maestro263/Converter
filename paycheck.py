# Calculate your monthly wage (with or without SU)

hours = float(input("How many hours have you worked: "))
HOURLYPAY = float(input("How much is your hourly pay?: "))


def calculate_wage():
    tax = hours * HOURLYPAY * 38 / 100
    global wage
    wage = hours * HOURLYPAY - tax
    print("You have made: ", wage)


def su():
    su_question = input("Do you receive SU? (Y/N): ")
    if su_question == "Y" or "y":
        print("You receive SU, so your wage has been added to the SU: ")
        wage_with_su = wage + 6000
        print("Your new wage with SU is: ", wage_with_su)
    else:
        print("You don't receive SU, so you wage stays the same: ", wage)


calculate_wage()
su()
