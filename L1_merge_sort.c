// Imports
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Constants
#define N 250000

// Globals
int x[N];

void merge_sort_O0(int *A, int p, int r);
void merge_sort_O3(int *A, int p, int r);
// Subroutines


// Printing Routine
void print_list(int *list, int n)
{
  for(int i = 0; i<n; i++)
    {
      printf(" %3d", list[i]);
    };
  printf("\n");
}


// Insertion Sort Routine 
void insertion_sort(int *list, int n)
{
  int key;
  int j;
  
  for(int i = 1; i < N; i++)
    {
      key = list[i];
      j = i - 1;

      while((j>=0) && (list[j]>key))
	{
	  list[j +1] = list[j];
	  j -= 1;
	};
      list[j+1] = key;
    };
}

// Main routine
int main(void)
{
  srand(time(NULL));
  printf("Lab1 - Insertion Sort\n\n");

  for(int i = 0; i < N; i++)
    {
      x[i] = (rand()>>24);
    }

//   printf("List before sorting\n");
//   print_list(x, N);

//   printf("\nList after sorting\n");
//   insertion_sort(x, N);
    merge_sort_O3(x, 0, N-1);
  // print_list(x, N);
  
  return 0;
}
