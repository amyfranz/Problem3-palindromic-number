def checkPalendrome(num):
  return str(num)[::-1] == str(num)

def findMultiple(num1, num2, digits = 0):
  arr = []
  minDigit = int('1' + ('0' * (digits-1)))
  for i in range (minDigit, num1):
    for j in range (minDigit, num2):
      if checkPalendrome(i * j):
        arr.append(i * j)
  return max(arr)
print(findMultiple(999, 999, 3))