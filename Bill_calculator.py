print("Welcome to Your Tip Calculator: ")
bill = float(input("What was the total Bill ?\n"))
percent = int(input("What percentage Tip would like to give ?\n"))
splitUp = int(input("How many people splitting the Bill ?\n"))

def bill_generation(bill,percent,splitUp):
  tip = (bill/100)*percent
  bill += tip
  return bill/splitUp
result = bill_generation(bill,percent,splitUp)
result = "{:.2f}".format(result)
print(f"Total bill for each is going to be: ${result}")