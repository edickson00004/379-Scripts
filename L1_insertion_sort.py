#Imports
from array import array
import random as r

# Insertion Sort
def insertion_sort(A, n):
	"""Sort a list or numpy array.

	Argument:
	A -- a list or numpy array
	n -- length of A
	"""
	# Traverse the list or array from index 1 to n-1.
	for i in range(1, n):
		key = A[i]

		# Insert A[i] into the sorted subarray a[0:i].
		# Compare stored key with the already sorted values to its left.
		# Move each item one position to the right until we find the 
		# position for the key or fall off the left end of the list or array.
		j = i - 1
		while j >= 0 and A[j] > key:
			A[j + 1] = A[j]
			j -= 1

		# Insert key at the correct position in the list or array.
		A[j + 1] = key
# Biggest
def longestRepeat(list, n):
        currentStreak = 0
        maxStreak = 0
        for i in range (n-1):
                if (list[i] != list[i+1]):
                        if (currentStreak > maxStreak):
                                maxStreak = currentStreak
                else:
                        currentStreak += 1
        return maxStreak
# Printing
def print_list(list, n):
        for i in range(0, n):
                print("%3d" % (list[i]), end="")
        print()


# Main Routine
def main():

        # Initial header
        print("Lab1 - Insertion sort")
        print()
        
        # For list to initialize array elements
        sortList = [5, 1, 7, 3, 1, 3, 9, 3, 3]
        N = len(sortList)

        # Print initialized elements and explanatory header
        print("List before sorting:")
        print_list(sortList, N)
        print()

        # Invoke insertion sort algorithm
        insertion_sort(sortList, N)

        # Print sorted list and explanatory header
        print("List after sorting:")
        print_list(sortList, N)

        print("Longest Repeat:")
        print(longestRepeat(sortList, N))

        
        
# Start-up Scripts
if __name__ == "__main__":
        main()
