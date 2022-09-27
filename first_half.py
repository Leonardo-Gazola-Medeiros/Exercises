def first_half(s):
    
    if (len(s)%2) != 0:
        return (s[0:((len(s)//2)+1)])
    else:
        return (s[0:((len(s[0:((len(s)//2))])))])
