def med_function(word1, word2, show_matrix):

    rows = len(word1)+1 
    cols = len(word2)+1

    T = [
        [0 for x in range(cols)] 
        for x in range(rows)]

    for i in range(1, rows):
        T[i][0] = i

    for j in range(1, cols):
        T[0][j] = j
        
    for col in range(1, cols):
        for row in range(1, rows):
            if str1[row-1] == str2[col-1]:
                sub_cost = 0
            else:
                sub_cost = 1
            T[row][col] = min(T[row-1][col] + 1,      
                                     T[row][col-1] + 1,    
                                     T[row-1][col-1] + sub_cost)
    
    if show_matrix:
        print("The MED matrix between " + str1 + " and " + str2 + " is: ")
        for r in range(rows):
            print(T[r])
    
    return T[row][col]

