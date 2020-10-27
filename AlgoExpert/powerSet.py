# def powerset(array, idx = None):
#     if idx is None:
#         idx = len(array)-1
#     if idx < 0:
#         return [[]]
#
#     element = array[idx]
#     subsets = powerset(array, idx-1) #subests returned in previous recurssion
#     #print(element, idx, subsets)
#
#     for i in range(len(subsets)): # the loop is to add the element to all the subsets
#         currentSubset = subsets[i]
#         subsets.append(currentSubset + [element])
#
#         #print("in for loop")
#         #print(currentSubset, element)
#
#         """
#         3 elemnts
#         in 3rd recussion [[]], [a] are returned
#         to this b is added in 2nd recurssion [] [a] [b] [a,b]
#         in first recurssion c is added [c] [ac] [bc] [abc]
#         """
#
#     return subsets

def powerset(array):

    subsets = [[]]

    for element in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [element])

    return subsets

array=["a", "b", "c"]
print(powerset(array))