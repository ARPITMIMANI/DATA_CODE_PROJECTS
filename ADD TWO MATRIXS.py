# ADD THE TWO MATRIXS OF MULTIPLE DIMENSIONS.

matrix1 = [ [12,14,16,18] , [20,22,24,26] , [28,30,32,34] , [36,38,40,42] ]
matrix2 = [ [44,46,48,50] , [52,54,56,58] , [60,62,64,68] , [70,72,74,76] ]

result = [ [0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0] ]

# ITERATE THROUGH ROWS .

for x in range ( len(matrix1) ) :
         
# ITERATE THROUGH COLUMNS .

        for y in range ( len(matrix1[0] ) ) :
                
                result[x][y] = matrix1[x][y] + matrix2[x][y]

# PRINT THE FINAL OUTPUT .

for z in result:
        print(z)