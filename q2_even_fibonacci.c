/*Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose 
values do not exceed four million, 
find the sum of the even-valued terms.
*/

// Answer: 4613732

#include <stdio.h>

int result = 0;// global result variable

void Fibonacci(int, int, int);

int main(void){
	Fibonacci(1, 1, 4000000);
	printf("%d\n", result);
	return 0;
}
// recursive fibonacci with max terminating condition
void Fibonacci(int prev, int cur, int max){
		int next = prev + cur;
		if (next > 4000000){
			return;
		}
		if (next % 2 == 0){
			result += next;
		}
		Fibonacci(cur, next, max);
	}