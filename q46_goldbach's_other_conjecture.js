/*
Stated problem:
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?\

Subproblems:
Is a number prime?
Is the conjecture true given a composite number?
Don't store all the primes in memory, generate them as needed.
*/

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

function testConjecture(num){
	if (num % 2 == 0){
		return false;
	}
	for (var i=2;i<=num-2;i++){
		if (isPrime(i)){
			if (isSquare((num-i)/2)){
				return true;
			}
		}
	}
	return false;
}

function isSquare(num){
	return Math.sqrt(num) % 1 == 0;
}

function disproveConjecture(){
	var num = 35;
	while (true){
		if (!isPrime(num)){
			if (!testConjecture(num)){
				return num;
			}
		}
		num += 2;
	}
}

console.log(disproveConjecture());