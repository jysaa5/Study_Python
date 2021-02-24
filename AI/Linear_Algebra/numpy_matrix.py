import numpy as np

def main():
    print(matrix_tutorial())

def matrix_tutorial():
    A = [
        [1, 4, 5, 8],
        [2, 1, 7, 3],
        [5, 4, 5, 9]
     ]
    #print(A)
    #print(np.array(A))
    A = np.array(A)
    return A

if __name__ == "__main__":
    main()
