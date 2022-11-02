# EXERCISE 1 --------------

def sum_to(n):
  sum = 0 
  for n in range(1, n + 1):
    sum += n
  return sum 

print('-----1-----')
print(sum_to(6))
print(sum_to(10))


# EXERCISE 2 --------------

def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest

print('-----2-----')
print(largest([1, 2, 3, 4, 0]))
print(largest(([10, 4, 2, 231, 91, 54])))


# EXERCISE 3 --------------