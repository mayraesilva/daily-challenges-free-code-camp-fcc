"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 5th, February, 2026.

----------------------------
Pocket Change
Given an array of integers representing the coins in your pocket, 
with each integer being the value of a coin in cents, 
return the total amount in the format "$D.CC".

100 cents equals 1 dollar.
In the return value, include a leading zero for amounts less than one dollar 
and always exactly two digits for the cents.
----------------------------
Tests
1. count_change([25, 10, 5, 1]) should return "$0.41".
2. count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]) should return "$1.43".
3. count_change([100, 25, 100, 1000, 5, 500, 2000, 25]) should return "$37.55".
4. count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]) should return "$0.70".
5. count_change([1]) should return "$0.01".
6. count_change([25, 25, 25, 25]) should return "$1.00".
"""

def count_change(change):
    total_cents = 0
    value = ''

    for coin in change: #calculating the total in cents
        total_cents += coin
    
    if total_cents < 10:
        value = f'$0.0{total_cents}'
        return value

    if total_cents < 100:
        
        value = f'$0.{total_cents}'
        print(value)
        return value
    
    else:

        dollars = total_cents // 100
        cents = total_cents % 100
        cents_string = f'{cents}'

        if cents == 0: 

            value = f'${dollars}.00'
            print(value)
            return value
        
        elif len(cents_string) == 1:

            value = f'${dollars}.0{cents}'
            print(value)
            return value
        
        else:

            value = f'${dollars}.{cents}'
            print(value)
            return value




count_change([25, 10, 5, 1])
count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25])
count_change([100, 25, 100, 1000, 5, 500, 2000, 25])
count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10])
count_change([1])
count_change([25, 25, 25, 25])