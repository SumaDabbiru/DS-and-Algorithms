def largestRange(array):
    longestRange = 0
    ranges = []
    nums = {}
    
    #create an Hashmap with boolen assigned to it
    for element in array:
        nums[element] = True
    
    #traverse through the array
    for num in array:
        #if the number is marked false in hashmap : continue if not nums[num]
        if nums[num] == False:
            continue
        #now set the number to false
        nums[num] = False
        
        currentlenght = 1
        
        left, right = num - 1, num + 1
        
        #check if the numbers less than the current number are present in the array
        #if yes change value of number to false in hashtable
        while left in nums:
            nums[left] = False
            currentlenght += 1
            left -= 1
        
        while right in nums:
            nums[right] = False
            currentlenght += 1
            right += 1
        
        if currentlenght > longestRange:
            longestRange = currentlenght
            ranges = [left+1, right-1]
            
    return ranges
        
        
    
    pass

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array))