def isPalindrome(x):
    y = x[::-1]
    if x == y: 
        return True
    else:
        return False
    
print(isPalindrome("donut"))