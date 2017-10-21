def selection_sort(array):
	source = array
	for i in range(len(source)):
	  mini = min(source[i:]) #find minimum element
	  min_index = source[i:].index(mini)-1 #find index of minimum element
	  source[i:][min_index]= source[i:][0] #replace element at min_index with first element
	  source[i:][0] = mini                  #replace first element with min element
	return source
	
if __name__ == "__name__":
##
##	