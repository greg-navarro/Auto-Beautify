# Using the 'resolution' from the umap file, estimate what the maximum size of an instance of 'noise' might be.
# Then search each element of the array to see if it is the center of such a noise instance.

# itertively remove isolated/discontinuous portions of the signal



def get_subset(two_d_array, i, j, threshold):
  subset = []
  current_operand = 0
  while current_operand <= threshold:
    print(current_operand)
    for element in get_layer(i, j, current_operand):
      print(element)
      subset.append(two_d_array[element[0]][element[1]])
    current_operand += 1
  return subset

def get_layer(i, j, operand):
  layer = []
  # edge case: operand is 0
  if operand == 0: 
    if valid_coord([i,j]):
      return [[i,j]]
    else:
      return []
  # calculate the 'least' coordinate location of this layer, in a four setp process collect all neighbor coordinates
  least_coord = [i-operand, j-operand]
  icurrent = least_coord[0]
  jcurrent = least_coord[1]  
  # [i - op, j - op] = [0 - 1, 0 - 1]
  # iterate over top of layer by iterating j upward
  while jcurrent < j + operand:
    print("first loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    jcurrent += 1
  # correct jcurrent
  # [i - op, j + op] = [0 - 1, 0 + 1]
  # jcurrent = j + operand
  # iterate 'downwards' over 'right' side of the layer
  while icurrent < i + operand:
    print("second loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    icurrent += 1
  # correct icurrent
  # [i + op, j + op] = [0 + 1, 0 + 1]
  # icurrent = i + operand
  # iterate 'leftwards' over 'bottom' side of the layer
  while jcurrent > j - operand:
    print("third loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    jcurrent -= 1
  #correct jcurrent
  # [i + op, j - op] = [0 + 1, 0 - 1]
  # jcurrent = j - operand
  # iterate 'upwards' over 'left' side of the layer
  while icurrent > least_coord[0]:
    print("fourth loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    icurrent -= 1
  return layer
  



def valid_coord(coord): 
  for element in coord:
    if not isinstance(element, int):
      return False
    if element < 0:
      return False
  return True


# x = get_layer(0,0,0)
# y = get_layer(0,0,1)
# z = get_layer(0,0,3)

# print(x)
# print(y)
# print(z)

test_2d_array = [[1,2,3], [4,5,6,],[7,8,9]]

print(get_subset(test_2d_array, 0, 0, 2))