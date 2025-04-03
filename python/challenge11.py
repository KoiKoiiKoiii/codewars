def get_middle(s):
    if len(s) % 2 == 0: # Check if the length of the string is Even
        return(f"{s[len(s) - round(len(s) / 2) - 1]}{s[len(s) - round(len(s) / 2)]}") 
    else:
        return(s[len(s) // 2]) 
