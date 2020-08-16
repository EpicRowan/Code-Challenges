# zero out matrix
 matrix =([
   ['A', 'B', 'C', 'D'],
   ['E', 'F',  0 , 'H'],
   ['I', 'J', 'K', 'L'],   
   ])

def zero_matrix(matrix):

	# count clusters of lists
	rows = len(matrix)
	# count first list
	cols = len(matrix[0])

	#if no matrix
	if not matrix:
    	return []

    # Make lists to keep track of which rows and columns we should clear
    clear_rows = [False] * rows   # [False, False, ...] x many rows as have
    clear_cols = [False] * cols   # [False, False, ...] x as many cols as have

    for x in range(rows):
    	for y in range(cols):
    		if matrix[x][y] == 0:
    			clear_rows[x] = True
    			clear_cols[y] = True

    # in sample matrix, clear_rows = [False, True, False]
    # clear_cols = [False, False, True, False]

    #clear rows and columns
    for y in range(rows):
        for x in range(cols):
            if clear_rows[y] or clear_cols[x]:
                matrix[y][x] = 0

    return matrix