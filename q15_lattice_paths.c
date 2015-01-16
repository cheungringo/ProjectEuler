/*Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?*/

#include <stdio.h>
#include <stdlib.h>

// this one is a little trickier algorithm wise
// was also asked this in my Microsoft interview

// algorithm is to create one 20 element array, then
// add 1 to the first element, then for the next 19 elements
// add the new previous element to it to get its new value

unsigned long long numPaths(int);

int main(void){
	printf("Number of paths for 20 by 20: %llu", numPaths(20));
	return 0;
}

unsigned long long numPaths(int n){
	unsigned long long array[n];
	for (int i=0;i<n;i++){
		array[i] = i+2;
	} // elements set 1 to 20
	for (int iter=1;iter<n;iter++){
		array[0] += 1;
		for (int i=1;i<n;i++){
			array[i] += array[i-1];
			printf("%llu\n", array[i]);
		}
	}
	return array[n-1];
}