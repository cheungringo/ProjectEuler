/*The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.*/

// this is a good algorithm, takes about 5 seconds

#include <stdio.h>
#include <stdlib.h>

int longest(int max){
	int start;
	int *possible = malloc(sizeof(int)*(max+1));
	if (possible == NULL){
		printf("Error");
		return 0;
	}
	for (int i=0;i<=max+1;i++){
		possible[i] = 1;
	}
	int longest = 1;
	for (int num=2;num<=max+1;num++){
		unsigned long i = num;
		if (possible[num] == 0){
			continue;
		}
		int count = 1;
		while (i != 1){
			if (i % 2 == 0){
				i /= 2;
				if (i < max+1){ // numbers can go over a million
					possible[i] = 0;
				}
				count ++;
			} else{
				i = 3*i + 1;
				if (i < max+1){ // numbers can go over a million
					possible[i] = 0;
				}
				count++;
			}
		}
		if (count > longest){
			longest = count;
			start = num;
		}
	}
	return start;
}

int main(void){
	printf("longest collatz sequence start with: %d\n", longest(1000000));
	return 0;
}