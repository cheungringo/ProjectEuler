/*
Stated problem: 
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

Subproblems: 
Get all 4 digit primes
Check if a number is a permutation of another
*/

function getPrimesOfDigit(n){
	var start = Math.pow(10, n-1);
	var end = Math.pow(10, n) - 1;
	return primesFrom(start, end);
}

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

function isPermOf(num, perm){
	var number = numToArray(num);
	var permutation = numToArray(perm);
	for (var i=0;i<number.length;i++){
		var index = permutation.indexOf(number[i]);
		if (index > -1){
			permutation.splice(index, 1);
		}
	}
	return permutation.length == 0 ? true : false;
}

function numToArray(num){
	var array = [];
	while (num > 0){
		array.push(num % 10);
		num = Math.floor(num/10);
	}
	return array;
}

function primePermutation(){
	var result = [];
	var primes = getPrimesOfDigit(4);
	for (var i=1488;i<primes.length;i++){
		var first = primes[i];
		for (var j=i+1;j<primes.length;j++){
			if (isPermOf(first, primes[j])){
				var second = primes[j];
				var third = second - first + second;
				if (isPermOf(first, third)){
					var index = primes.indexOf(third);
					if (index > -1){
						result.push(first);
						result.push(second);
						result.push(third);
						return result; 
					}
				}
			}
		}
	}
}

console.log(primePermutation());