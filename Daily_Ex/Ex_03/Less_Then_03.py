numbers = [1, 5, 10, 12, 20, 3, 4, 89, 21, 34, 5]
lessFnums = []
lessNnums = []

for num in numbers:
    if num < 5:
        lessFnums.append(num)
        lessFnums.sort()

print(lessFnums)


num = int(input("Enter a number: "))
for n in numbers:
    if n < num:
        lessNnums.append(n)
        lessNnums.sort()
    continue 

print(lessNnums)
        