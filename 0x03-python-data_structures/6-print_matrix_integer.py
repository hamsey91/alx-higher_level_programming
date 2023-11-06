def print_matrix_integer(matrix=[[]]):
  
    for row in matrix:
        for item in row:
            print(f"{item}", end=" " if item!=row[-1] else "")
        print()
