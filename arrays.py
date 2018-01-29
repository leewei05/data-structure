
numbers = [1,2,3,4,5]

# random indexing --> O(1) get items if we know the index !!
# print(numbers[0])

# for loop
# for num in numbers:
#     print(num)

# for sequence
# for i in range(len(numbers)):
#     print(numbers[i])

# [start index : end index]
print(numbers[0:2])

# [:] all fo the items
print(numbers[:])

# O(N) search running time
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
        
print(maximum)

