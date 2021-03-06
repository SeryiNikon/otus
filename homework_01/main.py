def power_numbers(*numbers):
    return list(map(lambda x: x ** 2, numbers))



# filter types
def is_prime(num):
    f=[]
    for i in num:
        if i==0 or i==1:
            f.append(i)
        for a in range(2, i):
            if i % a == 0:
                f.append(i)
                break
    return list(filter(lambda x: x not in f, num))

ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(number,func):
    if func == PRIME:
        return is_prime(number)
    if func == ODD:
        return list(filter(lambda x: x%2!=0, number))
    if func == EVEN:
        return list(filter(lambda x: x%2==0, number))
