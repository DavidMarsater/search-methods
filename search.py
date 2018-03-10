
'''
Showcases different search methods.
Does the list contain a pair of numbers, wich sum equals to x in a sorted list
'''

import time

items = [1, 3, 5, 6, 8, 15, 29]  # note! sorted list!
searchfor = 8


# just go through the list until the right number is found
def linear_search(items, desiredItem, startPos, endPos=None):
    if endPos == None:
        endPos = len(items)

    for i in range(startPos, len(items)):
        if items[i] == desiredItem:
            return i

    return None


# approximately halving the search area every time, asumes list is sorted
def binary_search(items, desiredItem, startPos, endPos=None):
    if endPos == None:
        endPos = len(items)

    if startPos == endPos:
        return None

    pos = (endPos - startPos)//2 + startPos  # split the search area in two

    if desiredItem == items[pos]:
        return pos
    elif desiredItem > items[pos]:  # return to a new search area
        return binary_search(items, desiredItem, startPos=pos+1, endPos=endPos)
    else:
        return binary_search(items, desiredItem, startPos=startPos, endPos=pos)


# start with the sum of the first and last element, asumes list is sortded
def custom(items, desiredSum, pointerOne, pointerTwo):

    if pointerOne == pointerTwo:  # no result
        return None

    if desiredSum == items[pointerOne]+items[pointerTwo]:
        result = {'pointerOne': pointerOne,
                  'pointerTwo': pointerTwo,
                  'numOne': items[pointerOne],
                  'numTwo': items[pointerTwo]
                  }
        return result

    # if the sum of the two elements is two large, then decrease the larger element
    elif desiredSum < (items[pointerOne]+items[pointerTwo]):
        pointerTwo -= 1
        return custom(items, desiredSum, pointerOne, pointerTwo)

    # if the sum of the two elements is two small, then increase the smaller element
    elif desiredSum > (items[pointerOne]+items[pointerTwo]):
        pointerOne += 1
        return custom(items, desiredSum, pointerOne, pointerTwo)


####################################################################################################
# now search for numbers in the three ways
# search for two numbers wich sum equals two x
# abort when a pair is found

# Linear search
start = time.perf_counter()
for i in range(0, len(items)):
    if i >= searchfor:  # assume there are no more
        break
    result = linear_search(items, searchfor-items[i], 0, None)  # search for the number needed for a sum = searchfor
    if result != None:  # abort when a pair is found
        result = {
            'numOne': items[i],
            'numTwo': items[result]
        }
        break
#processtime_linear = time.perf_counter() - start
print('Linear_result: '+str(result))
processtime_linear = time.perf_counter() - start


# binary search
start = time.perf_counter()
for i in range(0, len(items)):
    if i >= searchfor:  # assume there are no more
        break
    result = binary_search(items, searchfor-items[i], 0, None)
    if result != None:  # abort when a pair is found
        result = {
            'numOne': items[i],
            'numTwo': items[result]
        }
        break
processtime_binary = time.perf_counter() - start
print('Binary_result: '+str(result))

# custom mojo search
start = time.perf_counter()
result = custom(items, searchfor, 0, len(items)-1)
processtime_custom = time.perf_counter() - start
print('Custom_result: '+str(result))


print('Search time_Linear: '+str(processtime_linear))
print('Search time_binary: '+str(processtime_binary))
print('Search time_custom: '+str(processtime_custom))
