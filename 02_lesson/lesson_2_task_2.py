def is_year_leap(year):
    return year % 4 == 0

year = int(input())
result = is_year_leap(year)
print(f"год {year}: {result}")