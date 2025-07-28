def bonAppetit(bill, k, b):
    total_bill = sum(bill) - bill[k]
    anna_should_pay = total_bill // 2

    if anna_should_pay == b:
        print("Bon Appetit")
    else:
        print(b - anna_should_pay)

# Input format as per HackerRank
n, k = map(int, input().split())
bill = list(map(int, input().split()))
b = int(input())

bonAppetit(bill, k, b)
