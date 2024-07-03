# I am assuming I can't use sorted() either

def maxmin(numbers):
    maxx = numbers[0]
    minn = numbers[0]
    for i in numbers:
        if i>maxx:
            maxx = i
        if i<minn:
            minn = i
    return [minn,maxx]

nums = input("Please enter a series of numbers, separated only by \',\': ").split(",")
print(maxmin(list(map(int,nums))))
