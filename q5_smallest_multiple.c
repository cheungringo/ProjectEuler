/*2520 is the smallest number that can be divided by each of 
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?*/

// Answer: 232792560

// this one is kind of silly since we know that the primes
// 11 13 17 19 have to be multiplied and then we just need
// another 2 from the 16, so just multiply 2520 by these numbers
// a more modular version would be to iterate up to the max, 
// with each time checking if we need to multiply in any more
#include <stdio.h>

void smallest(int, int *);

int main(){
	int result = 2520;
	smallest(20, &result);
	printf("%d\n", result);
}

void smallest(int max, int *result){
	for (int i=11;i<=max;i++){
		int temp = i;
		for (int j=i-1;j>1;j--){
			if (temp % j == 0){
				temp /= j;
				// a hack fix for 16 since we need a way of checking prime factorization
				if (j == 8 && temp % 2 == 0){
					break;
				}
			}
		}
		printf("%d\n", temp);
		*(result) *= temp;
	}
}