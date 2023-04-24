let rec binary_search element arr startIndex endIndex =
	if startIndex > endIndex
	then -1
	else let middleIndex = (startIndex + endIndex) / 2 in
		 if arr[middleIndex] = element then middleIndex 
		 else if element < arr[middleIndex] 
		 then binary_search element arr middleIndex endIndex
		 else binary_search element arr startIndex middleIndex 