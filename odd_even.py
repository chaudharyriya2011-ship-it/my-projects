start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
even = []
odd = []
for i in range(start, end+1):
    sqr = i*i
    if sqr % 2 == 0:
        even.append(sqr)
    else:
        odd.append(sqr)
print("Even: " , even)
print("odd: " , odd)