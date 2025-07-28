import math

# Function to calculate LCM of a list
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_list(arr):
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)
    return result

# Function to calculate GCD of a list
def gcd_list(arr):
    result = arr[0]
    for num in arr[1:]:
        result = math.gcd(result, num)
    return result

def getTotalX(a, b):
    l = lcm_list(a)
    g = gcd_list(b)

    count = 0
    multiple = l
    while multiple <= g:
        if g % multiple == 0:
            count += 1
        multiple += l
    return count

# Input handling
if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    print(getTotalX(a, b))
