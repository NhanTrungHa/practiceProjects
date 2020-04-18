import pyinputplus as pyip

cheeseChoice = ""

print("Pick your bread: ")
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)

print("Pick your protein: ")
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)

print("Do you want cheese?: ")
cheese = pyip.inputYesNo()
if cheese:
    cheeseChoice = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)

print("Do you want a sauce?: ")
sauce = pyip.inputYesNo()

print("How many sandwiches do you want?: ")
amount = pyip.inputInt()

price = 0
breadPrices = {"wheat": 1.5, "white": 1, "sourdough": 2}
proteinPrices = {"chicken": 3, "turkey": 3, "ham": 4, "tofu": 0}
cheesePrices = {"cheddar": 1, "Swiss": 2, "mozzarella": 1}
for i in breadPrices:
    if i == bread:
        price += breadPrices[i]
for i in proteinPrices:
    if i == protein:
        price += proteinPrices[i]
for i in cheesePrices:
    if i == cheeseChoice:
        price += cheesePrices[i]
price *= amount

print(price)

