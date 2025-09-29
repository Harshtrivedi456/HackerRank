def timeInWords(h, m):
    words = ["zero","one","two","three","four","five","six","seven","eight","nine","ten",
             "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
             "eighteen","nineteen","twenty"]
    for i in range(21, 30):
        words.append("twenty " + words[i-20])
    if m == 0:
        return f"{words[h]} o' clock"
    elif m == 15:
        return f"quarter past {words[h]}"
    elif m == 30:
        return f"half past {words[h]}"
    elif m == 45:
        return f"quarter to {words[h%12+1]}"
    elif m < 30:
        return f"{words[m]} minute{'s'*(m>1)} past {words[h]}"
    else:
        return f"{words[60-m]} minute{'s'*(60-m>1)} to {words[h%12+1]}"

if __name__ == "__main__":
    h = int(input())
    m = int(input())
    print(timeInWords(h, m))
