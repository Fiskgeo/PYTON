def is_year_leap (year):

    if year % 4 == 0:
        return True
    else:
        return False


# Test 1
year_control = 2024
result = is_year_leap(year_control)
print(f"Год {year_control}: {result}")


# Test 2
year_control = 2025
result = is_year_leap(year_control)
print(f"Год {year_control}: {result}")
