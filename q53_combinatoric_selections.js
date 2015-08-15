/*
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	
n!/(r!(n−r)!)
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

Subproblems:
Find the lowest value of r that is greater than one million for a given n
Then since nCr mirrors, can figure out for how many values of r exceed one million by doing n - 2*r + 1
*/

function selectCombinatorics(){
	var num = 0;
	for (var n=23;n<=100;n++){
		for (var r=1;r<n;r++){
			if (choose(n, r) > 1000000){
				num += n - 2*r + 1;
				break;
			}
		}
	}
	return num;
}

function choose(n, r){
	return fact(n)/(fact(r)*fact(n-r));
}

function fact(n){
	if (n == 1){
		return 1;
	}
	else {
		return n * fact(n-1);
	}
}

console.log(selectCombinatorics());