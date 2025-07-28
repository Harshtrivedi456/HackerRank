
def timeConversion(s):
    period = s[-2:]       # AM or PM
    hh = int(s[:2])        # hour part as integer

    if period == "AM":
        if hh == 12:
            hh = 0
    else: # PM
        if hh != 12:
            hh += 12

    # format back to string with leading zeros
    return "{:02}:{:02}:{:02}".format(hh, int(s[3:5]), int(s[6:8]))

# Example usage
s = input()
print(timeConversion(s))
