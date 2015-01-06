/*
If p is the perimeter of a right angle triangle with integral length 
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
*/
//we can approximate that using euclid, the max for m is 
// sqrt(1000) approx 33
// remember that euclid's only generates unique triples if
// m > n, m - n is odd and m, n are coprime

#include <stdio.h>
#include <stdlib.h>
int getTriple(int, int);
int coprime(int, int);
int main(void){
	int high = 1001;
	int* count = malloc(sizeof(int)*high);
	for (int i=0;i<high;i++){
		count[i] = 0;
	}
	for (int m=1;m<33;m++){
		for (int n=1;n<m;n++){
			if ((m - n) % 2 == 0 ){
				continue;
			}
			if (coprime(m,n) == 0){
				continue;
			}
			int max = getTriple(m, n);
			if (max > 1000){
				continue;
			} do{
				count[max]++;
				max += max;
			}while (max <= 1000);
		}
	}
	int greatest = 0;
	int max;
	for (int i=0;i<1001;i++){
		if (count[i] > greatest){
			greatest = count[i];
			max = i;
		}
	}
	printf("%d", max);
	return 0;
}
int coprime(int m, int n){
	while (1){
		if (m > n){
			m = m % n;
		}
		else{
			n = n % m;
		}

		if (m == 0 || n == 0){
			return 1;
		}
		if (m == 1 || n == 1){
			return 0;
		}
	}	
}

int getTriple(int m, int n){
	// returns the sum of this triple
	int a = (m*m - n*n);
	int b = 2*m*n;
	int c = (m*m+n*n);
	return a+b+c;
}