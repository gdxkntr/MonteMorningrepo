 #make an array for sorting selction
 array = [13,4,9,5,3,16,12]

#defines function selectionsort for array
 def SelectionSort(array):

 	#range = checks length of array
 	n = len(array)

 	#for var i (minimum value) of range(defined above)
 	for i in range(n): #<-- whatever the len/however many times youll run the for loop

 		#initally assume first element of unsorted part as minimum.

 		minimum = i 
 		#j = number in array (minimum+1,calls len of array)
 		for j in range(i+1,n):

 			if (array[j] < array[minimum]):

 			minimum = j


 		#instantiates a temporary value for minimum in array
 		temp = array[i]
 		#recalls instantiates the i as array minimum
 		array[i] = array minimum
 		#recalls minimum in array is temporary
 		array[minimum] = temp

 	#returns the array after numbers have been sorted
 	return array
 
 #prints the result
 print(SelectionSort)