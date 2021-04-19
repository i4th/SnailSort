
def snail_search(array):

  sequence = []
  if not array:
    return str([sequence])

  rows = len(array)
  colu = len(array[0])

  print('ROWS: ' + str(rows))
  print('COLU: ' + str(colu))

  i = 0
  j = 0
  # TOP ROW FROM LEFT TO RIGHT
  while i < len(array):
    sequence.append(array[j][i])
    print(array[j][i])
    i = i + 1
  i = i - 1

  # TOP RIGHT TO BOTTOM RIGHT
  print('I IS CURRENTLY: ' + str(i))  
  print('J IS CURRENTLY: ' + str(j))  

  while j < len(array[0]):
    sequence.append(array[j][i])
    print(array[j][i])
    j = j + 1
  j = j - 1

  # BOTTOM RIGHT TO BOTTOM LEFT
  print('I IS CURRENTLY: ' + str(i))  
  print('J IS CURRENTLY: ' + str(j))  

  while i >= 0:
    sequence.append(array[j][i])
    print(array[j][i])
    i = i - 1
  i = i + 1

  # UP A BIT 
  print('I IS CURRENTLY: ' + str(i))  
  print('J IS CURRENTLY: ' + str(j)) 

  return sequence

###############

array_1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print('TESTING ARRAY 1')
print(snail_search(array_1))
print('_______________________')

array_2 = [[1,2],
          [3,4]]

print('TESTING ARRAY 2')
print(snail_search(array_2))
print('_______________________')

array_3 = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

print('TESTING ARRAY 3')
print(snail_search(array_3))
print('_______________________')

print('TESTING EMPTY ARRAY')
array_empty = []
print(snail_search(array_empty))
print('_______________________')