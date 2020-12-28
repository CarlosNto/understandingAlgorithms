def binary_search(list, item): #must be an ordered list
  low = 0 
  high = len(list) -1
  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else: low = mid + 1
  return none

my_list = [1, 3, 5, 7, 9, 17, 53, 71, 89, 98]
binary_search(my_list, 53) # the output will be the index position of these number,53 -> (i = 6)
