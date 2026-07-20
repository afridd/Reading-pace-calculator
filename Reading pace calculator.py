pages = int(input("Enter the number of pages: "))
days = int(input("Enter the number of days: "))

if pages <= 0 or days <= 0:
    print("You must enter value greater than 0")
else:
    calculation = pages / days
    
    pages_per_day = int(calculation) if calculation.is_integer() else round(calculation, 2)
  
    page_str = "page" if pages_per_day == 1 else "pages"
    days_str = "day" if days == 1 else "days"  
    
    print(f"\nYou must read {pages_per_day} {page_str} to complete the book in {days} {days_str}")
  
