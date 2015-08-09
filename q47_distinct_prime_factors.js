/*
Stated problem:
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

Subproblems:
Prime factor a number in a loop of num
break the loop if the length of distinct prime factors is not num or the number is prime
if the loop is not broken num times, then return the start of the loop
*/

function distinctPrimeFactors(num){
	var factors = [];
	var divisible = false;
	while (num % 2 == 0){
		divisible = true;
		num /= 2;
	}
	if (divisible == true){
		factors.push(2);
	}
	var factor = 3;
	divisible = false;
	while (num != 1){
		if (isPrime(factor)){
			while (num % factor == 0){
				divisible = true;
				num /= factor;
			}
			if (divisible == true){
				factors.push(factor);
			}
		}
		divisible = false
		factor += 2;
	}
	return factors;
}

function isPrime(num){
	if (num % 2 == 0 || num < 2){
		return false;
	}
	for (var i=3;i<Math.sqrt(num);i+=2){
		if (num % i == 0){
			return false;
		}
	}
	return true;
}

function findConsecutive(num){
	/*
	Returns the first number of num consecutive numbers to have num distinct prime factors.
	*/
	var start = 2;
	while (true){
	    var found = true;
		for (var i=start;i<start+num;i++){
			if (isPrime(i)){
				found = false;
				break;
			}
			if (distinctPrimeFactors(i).length != num){
			    found = false;
				break;
			}
		}
		if (found){
		    return start;
		}
		start += 1;
	}
}


console.log(findConsecutive(2));