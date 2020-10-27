# def permutations(array):
#     """
#     Recusrrion
#     copied from algo expert
#     :param array:
#     :return:
#     """
#     permutations = []
#     permutationsHelper(0, array, permutations)
#     return permutations
#
# def permutationsHelper(i, array, permutations):
#     if i == len(array) - 1:
#         permutations.append(array[:])
#
#     else:
#         for j in range (i,len(array)):
#             array[i], array[j] = array[j], array[i]
#             permutationsHelper(i+1, array, permutations)
#             array[i], array[j] = array[j], array[i]

def permutations(array):
    """
:(
    from algo expert
    :param array:
    :return:
    """
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)

    else:
        for i in range (len(array)):
            newArray = array[: i] + array[i + 1 :]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(newArray, newPermutation, permutations)




array=[1,2,3]

print(permutations(array))
