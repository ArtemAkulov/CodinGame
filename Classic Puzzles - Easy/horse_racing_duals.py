#########################################
#                                       #
#  CodinGame Classic Puzzles  -  Easy   #
#         Horse-Racing Duals            #
#                                       #
#########################################

def heapsort(aList):
    length = len( aList ) - 1
    leastParent = length / 2
    
    for i in range ( int(leastParent), -1, -1 ):
        moveDown( aList, i, length )
    for i in range ( length, 0, -1 ):
        if aList[0] > aList[i]:
            swap( aList, 0, i )
        moveDown( aList, 0, i - 1 )
 
def moveDown( aList, first, last ):
    largest = 2 * first + 1
    while largest <= last:
        if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
            largest += 1
        if aList[largest] > aList[first]:
            swap( aList, largest, first )
            first = largest;
            largest = 2 * first + 1
        else:
            return
 
def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

array_to_sort = []
n = int(input())
for i in range(n):
    pi = int(input())
    array_to_sort.append(pi)
heapsort(array_to_sort)
resulting_value = abs(array_to_sort[len(array_to_sort) - 1] - array_to_sort[0])
for i in range(len(array_to_sort) - 1):
    if abs(array_to_sort[i + 1] - array_to_sort[i]) < resulting_value:
        resulting_value = abs(array_to_sort[i + 1] - array_to_sort[i])
print(resulting_value)