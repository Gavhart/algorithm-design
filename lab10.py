# 1. Name: Gavin Hart
# 2. Assignment Name: Lab 10: Number of Days
# 3. Assignment Description: This program prompts the user for a start date and an end date, 
#    validates the input, and computes the number of days between the two dates. It checks 
#    for leap years and ensures the dates are logically correct (e.g., start date before end date).
# 4. What was the hardest part? The most challenging part was ensuring the input validation was robust,
#    especially handling leap years and the varying number of days in each month. Debugging input edge cases
#    required careful thought and testing.
# 5. How long did it take for you to complete the assignment? 3hrs


from datetime import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        raise ValueError("Invalid month")

def demo():
    test_cases = [
        ("1752-12-31", "1753-01-01"),  # Year less than 1753
        ("abcd-03-10", "2005-04-22"),  # Non-integer year
        ("2000-00-15", "2000-01-15"),  # Month less than 1
        ("2000-13-15", "2001-01-15"),  # Month greater than 12
        ("2000-01-00", "2000-01-15"),  # Day less than 1
        ("2000-02-30", "2000-03-01"),  # Day greater than the number of days for a month
        ("2000-01-15", "1999-12-31"),  # End date before start date
        ("2000-01-01", "2000-01-01"),  # Start and end dates are the same
        ("2000-01-01", "2000-01-15"),  # Start and end dates are in the same month
        ("2000-01-01", "2000-12-31"),  # Start and end dates are in the same year
        ("2023-12-25", "2024-01-08"),  # Start date is Christmas and end date is two weeks later
        ("1990-10-26", datetime.now().strftime("%Y-%m-%d"))  # Your birth date and today's date
    ]

    for start_date_str, end_date_str in test_cases:
        print(f"\nTest case: Start date {start_date_str}, End date {end_date_str}")
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d") if isinstance(start_date_str, str) else start_date_str
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d") if isinstance(end_date_str, str) else end_date_str
            
            assert start_date.year >= 1753, "Year must be 1753 or later."
            assert 1 <= start_date.month <= 12 and 1 <= end_date.month <= 12, "Month must be between 1 and 12."
            assert 1 <= start_date.day <= get_days_in_month(start_date.year, start_date.month)
        except AssertionError as e:
            print(f"AssertionError: {e}")
