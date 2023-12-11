year = 1992
leap = False
print(f"{year%4},{year%100},{year%400}")
# Leap is True if 
# 1. If year can be divided by 4 evenly
# 2. If year can evenly divided by 100 and then it should be evenly
#    dividable by 400 as well
def is_leap(year):
    leap = False
    if (year % 4) == 0:
        leap = True
        if (year % 100) == 0:
            leap = False
            if (year % 400) == 0:
                leap = True            
        else:
            leap = True    
    return leap  

print(is_leap(year))   