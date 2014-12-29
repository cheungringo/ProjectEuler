/*The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?*/

// Answer: 6857

/* for this question, just do prime factorization 
until a reasonably small number. i.e. use a sieve to get prime numbers
then run through each one until the square root of the current quotient
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int* sieve(int, int);

int main(void){
	unsigned long long int num = 600851475143;
	//scanf("%llu\n", &num);
	//printf("%llu\n", num);
	int *primes = sieve(2, 10000);
	for (int i=1;i<=primes[0];i++){
		if (primes[i] == num){
			break;
		}
		while (num % primes[i] == 0){
			num /= primes[i];
		}
	}
	printf("%llu\n", num);
	return 0;
}

int* sieve(int low, int high){
	int *temp = malloc(sizeof(int)*high);
	for (int i=0;i<high;i++){
		temp[i] = 0;
	}
	int prime = 2;
	while (prime <= high){
		if (temp[prime] == 1){
			prime++;
			continue;
		}
		int mark = prime * prime;
		while (mark <= high){
			temp[mark] = 1;
			mark += prime;
		}
		prime++;
	}
	int j = 1;
	int *primes = malloc((high-low)*sizeof(int));
	for (int i=low;i<high;i++){
		if (temp[i] == 0){
			primes = realloc(primes, sizeof(primes)+sizeof(int));
			primes[j] = i;
			j++;
		}
	}
	primes[0] = j-1;
	free(temp);
	temp = NULL;
	return primes;
}