pages = int(input("Enter the number of pages: "))
days = int(input("Enter the number of days: "))

if pages <= 0 or days <= 0:
  print("You must enter value greater than 0")
else:
  calculation = pages/days
  if calculation.is_integer():
      pages_per_day = int(calculation)
  else:
     pages_per_day= round(calculation,2)
  
 
  if pages_per_day == 1 and days == 1:
    print(f"You must read {pages_per_day} page to complete the book in {days} day")
  elif pages_per_day==1 and days>1:
    print(f"You must read {pages_per_day} page to complete the book in {days} days")
  elif pages_per_day>1 and days==1:
    print(f"You must read {pages_per_day} pages to complete the book in {days} day")
  elif pages_per_day>1 and days>1:
    print(f"You must read {pages_per_day} pages to complete the book in {days} days")
  else:
    print(f"You must read {pages_per_day} pages to complete the book in {days} days")
