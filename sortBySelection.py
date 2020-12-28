def searchSmaller(arr):
  smaller = arr[0] #keeps the smallest index
  smaller_index = 0 #keeps the index of the smallest value
  for i in range(1, len(arr)):
    if arr[i] < smaller:
      smaller = arr[i]
      smaller_index = i
  return smaller_index

def sortBySelection(arr): #sorting an array
  newArr = []
  for i in range(len(arr)):
    smaller = searchSmaller(arr) #find the smallest element inside of array and place it int the new array
    newArr.append(arr.pop(smaller))
  return newArr
  
  arr1 = [ 9, 33, 21, 53, 74, 62, 97, 1, 13]
  sortBySelection(arr1)
