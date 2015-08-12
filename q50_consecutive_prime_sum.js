/*
Stated problem:
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, 
and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Subproblems:
Generate primes below one million
Check if each prime can be written as the sum of consecutive primes.
Store the number of consecutive primes, if higher, then replace.
*/

function primesFrom(start, end){
	var array = [];
	for (var i=0;i<end+1;i++){
		array.push(1);
	}
	for (var i=2;i<end+1;i++){
		if (array[i] == 0){
			continue;
		}
		else {
			for (var j=Math.pow(i, 2);j<end+1;j += i){
				array[j] = 0;
			}
		}
	}
	var primes = [];
	for (var i=start; i < end+1;i++){
		if (array[i] == 1){
			primes.push(i);
		}
	}
	return primes;
}

function longestConsecutivePrimes(below){
	var prime = 0;
	var primes = primesFrom(2, below);
	var consecutive = getMax(primes, below);
	for (;;){
		prime = tryConsecutive(primes, consecutive, below);
		if (prime != 0){
			//console.log("Consecutive: ", consecutive);
			return prime;
		}
		consecutive -= 1;
	}

}

function tryConsecutive(primes, consecutive, below){
	/*
	checks all the consecutive sums that are consecutive long,
	if any are prime and below the below threshold, return it.
	*/
	var start = 0;
	while (true){
		var total = 0;
		for (var i=start;i<start+consecutive;i++){
			total += primes[i];
		}
		if (total > below){
			return 0;
		}
		if (primes.indexOf(total) > -1){
			return total;
		}
		start += 1;
	}
	return 0;
}

function getMax(primes, below){
	var consecutive = 0;
	var total = 0;
	var i = 0;
	while (true){
		total += primes[i];
		i += 1;
		consecutive += 1;
		if (total > below){
			break;
		}
	}
	return consecutive;
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

console.log(longestConsecutivePrimes(1000000));