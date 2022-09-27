
def dista10(n):
    if ((n - 100 <= 10 and n - 100 > 0) or (100 - n <= 10 and 100 - n > 0)) or ((n - 200 <= 10 and n - 200 >0) or (200 - n <= 10 and 200 - n >0)):
        return True
    else:
        return False