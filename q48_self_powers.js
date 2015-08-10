/*
Stated problem:
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

Subproblems:
We only need to keep ten digits and just keep adding those ten digits.
Whenever we get to a number whose base is divisible by ten, just skip that number
because when it is multiplied by itself whatever number of times, the last ten digits
will be zeroes for sure.
Figure out the last ten digits in n^n.
*/

function selfPower(n){
	var result = n;
	for (var i=1;i<n;i++){
		result = (result * n) % 10000000000;
	}
	return result;
}

function sumPowersTo(n){
	var sum = 0;
	for (var i=1;i<=n;i++){
		sum = (sum + selfPower(i)) % 10000000000;
	}
	return sum;
}
console.log(sumPowersTo(1000));
