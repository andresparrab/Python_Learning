def median(original_list):
    length_list= len(original_list)
    original_list.sort()
    middle= int(length_list/2)
    if (length_list % 2) == 0:
        #mean will be the middle index, that is middle-1 plus next number in the index, middle and divide by 2 to get the mean.
        mean=(original_list[middle]+original_list[middle-1])/2
        return mean
    else:
        return original_list[middle]
print(median([4,5,5,4]))
