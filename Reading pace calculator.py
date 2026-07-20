pages= int(input("Enter the number of pages: "))
days = int(input("Enter the number of days: "))

if pages <= 0 or days <= 0:
  print("You must enter value greater than 0")
else:
  calculation = pages/days
  
  # Consolidate integer check into a single line
  pages_per_day = int(calculation) if calculation.is_integer() else pages_per_day= round(calculation,2)
    
  # Use inline conditional logic inside the f-string to handle pluralization  
  page_str="page" if pages_per_day==1 else page_str="pages"
  days_str="day" if days==1 else days_str="days"  
  
  print(f"\nYou must read {pages_per_day} {page_str} to complete the book in {days} {days_str}")
  
