#Imports
from array import array
import random as r

# Constants
N = 10

# Globals
x = array('i', [0]*N)

# Subroutines
def merge(A, p, q, r):

    if type(A) is list:
        left = A[p:q+1]
        right = A[q+1: r+1]
    else:
        left =      A[p:q+1]
        right =      A[q+1: r+1]

    i = 0
    j = 0
    k = p

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1

        k += 1

    if i < len(left):
        A[k : r+1] = left[i:]
    if j < len(right):
        A[k : r+1] = right[j:]
            
def merge_sort(A, p = 0, r = None):

    if r is None:
        r = len(A) - 1
    if p >= r:
        return
    q = (p+r)//2
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)

# Printing
def print_list(list, n):
    for i in range(0, n):
        print("%3d" % (list[i]), end="")
    print()

# Main Routine
def main():

    # Initial Header
    print("Lab1 - Merge Sort")
    print()

    # For list to initialize array elements
    for i in range(0, N):
        x[i] = r.randint(0, 99)

    # Print initialized elements and explanatory header
    print("List before sorting:")
    print_list(x, N)
    print()

    # Invoke merge sort algorithm
    merge_sort(x)

    # Print sorted list and explanatory header
    print("List after sorting:")
    print_list(x, N)
    
# Start-up Scripts
if __name__ == "__main__":
    main()

    
