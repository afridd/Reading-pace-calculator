# Daily Reading Calculator 📖

A simple and efficient Python script that helps you plan your reading schedule. By entering the total number of pages in a book and your target completion time in days, the program calculates exactly how many pages you need to read each day.

## Features
* **Smart Formatting:** Outputs clean whole numbers if the math divides evenly, and rounds to two decimal places if it doesn't.
* **Grammar Aware:** Dynamically adjusts the output to use singular or plural words ("page" vs "pages", "day" vs "days") based on your inputs.
* **Input Validation:** Prevents errors by ensuring the user enters values greater than 0. 

## Requirements
* **Python 3.6 or higher** (The script uses f-strings for formatting).

## How to Use
1. Save the code in a file named `reading pace calculator.py`.
2. Open your terminal or command prompt.
3. Run the script using the following command (the quotes are required because of the spaces in the filename):
   ```bash
   python "reading pace calculator.py"
   ```
4. Follow the on-screen prompts to enter your numbers.

## Example Output

**Example 1: Even division (plural output)**
```text
Enter the number of pages: 300
Enter the number of days: 10
You must read 30 pages to complete the book in 10 days
```

**Example 2: Decimal division (grammar adjustment)**
```text
Enter the number of pages: 350
Enter the number of days: 6
You must read 58.33 pages to complete the book in 6 days
```

**Example 3: Singular grammar**
```text
Enter the number of pages: 1
Enter the number of days: 1
You must read 1 page to complete the book in 1 day
```

**Example 4: Error handling**
```text
Enter the number of pages: 0
Enter the number of days: 5
You must enter value greater than 0
```
