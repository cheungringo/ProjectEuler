/*
Stated problem:
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

Subproblems:
Get a list of primes
Be able to convert them back and forth from array form
Check if a number is prime
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

function numToArray(num){
	var array = [];
	while (num > 0){
		array.unshift(num % 10);
		num = Math.floor(num/10);
	}
	return array;
}

function isRepeatedDigit(array){
	for (var i=0;i<array.length;i++){
		for (var j=0;j<array.length;j++){
			if (array[i] == array[j]){
				return true;
			}
		}
	}
	return false;
}

function arrayToNum(array){
	var length = array.length;
	var num = 0;
	for (var i=0;i<length;i++){
		num += array[i]*Math.pow(10, length-i-1);
	}
	return num;
}

function findSmallestRepeat(num){
	var primes = primesFrom(56000, 150000);
	var count = 0;
	for (var i=0;i<primes.length;i++){
		var currentArray = numToArray(primes[i]);
		if (!isRepeatedDigit(currentArray)){
			continue;
		}
		if (checkReplacements(currentArray, num)){
			return arrayToNum(currentArray);
		}
	}
	return "Increase upper limit";
}

function checkReplacements(array, num){
	if (!searchTwo(array, num)){
		return searchThree(array, num);
	}
}

function searchTwo(array, num){
	for (var i=0;i<array.length;i++){
		for (var j=i+1;j<array.length;j++){
			if (array[i] == array[j]){
				var temp = cloneArray(array);
				var count = 1;
				for (var k=0;k<10;k++){
					if (temp[i] == 9 && i == 0){
						temp[i] = 1;
						temp[j] = 1;
					}
					else if (temp[i] == 9){
						temp[i] = 0;
						temp[j] = 0;
					}
					else {
						temp[i] += 1;
						temp[j] += 1;
					}
					if (temp[i] == array[i] && temp[j] == array[j]){
						break;
					}
					if (isPrime(arrayToNum(temp))){
						count += 1;
					}
				}
				if (count == num){
					return true;
				}
			}
		}
	}
	return false;
}

function cloneArray(array){
	var temp = [];
	for (var l=0;l<array.length;l++){
		temp.push(array[l]);
	}
	return temp;
}

function searchThree(array, num){
	for (var i=0;i<array.length;i++){
		var found = array.indexOf(array[i], i+1);
		if (found > i){
			var foundAgain = array.indexOf(array[i], found+1);
			if (foundAgain > found){
				var count = 1;
				var temp = cloneArray(array);
				for (var k=0;k<10;k++){
					if (temp[i] == 9 && i == 0){
						temp[i] = 1;
						temp[found] = 1;
						temp[foundAgain] = 1;
					}
					else if (temp[i] == 9){
						temp[i] = 0;
						temp[found] = 0;
						temp[foundAgain] = 0;
					}
					else {
						temp[i] += 1;
						temp[found] += 1;
						temp[foundAgain] += 1;
					}
					if (temp[i] == array[i] && temp[found] == array[found] && temp[foundAgain] == array[foundAgain]){
						break;
					}
					if (isPrime(arrayToNum(temp))){
						count += 1;
					}
				}
				if (count == num){
					return true;
				}
			}
		}
	}
}

console.log(findSmallestRepeat(8));