 
 #make an array for sorting selction

 array = [13,4,9,5,3,16,12]

 def SelectionSort(array):

 	n = len(array)

 	for i in range(n): #<-- whatever the len/however many times youll run the for loop

 		#initally assume first element of unsorted part as minimum.

 		minimum = i 

 		for j in range(i+1.n):

 			if (array[j] < array[minimum]):

 			minimum = j



 		temp = array[i]
 		array[i] = array minimum
 		array[minimum] = temp

 	return array
 	
 print(SelectionSort(array))


