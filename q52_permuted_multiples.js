/*
Stated problem:
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, 
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Subproblems:
Check if two numbers contain the same digits.
Convert number to array, check each number of array.
*/

function numToArray(num){
	var array = [];
	while (num > 0){
		array.unshift(num % 10);
		num = Math.floor(num/10);
	}
	return array;
}

function arrayToNum(array){
	var length = array.length;
	var num = 0;
	for (var i=0;i<length;i++){
		num += array[i]*Math.pow(10, length-i-1);
	}
	return num;
}

function matchDigits(array1, array2){
	if (array1.length != array2.length){
		return false;
	}
	var indices = [];
	for (var i=0;i<array1.length;i++){
		var where = array2.indexOf(array1[i]);
		if (where < 0){
			return false
		}
		if (indices.indexOf(where) > -1){
			return false;
		}
		indices.push(where);
	}
	return true;
}

function findX(){
	var x = 1;
	for (;;){
		for (var i=2;i<7;i++){
			if (!matchDigits(numToArray(x), numToArray(i*x))){
				break;
			}
			if (i == 6){
				return x;
			}
		}
		x += 1;
	}
}

console.log(findX());