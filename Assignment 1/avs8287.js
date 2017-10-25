//Anena Sims
//1001138287
//10/2/2017
//Code executed in Mac terminal using node avs8287.js


//1) Starting array (no restrictions on initialzing the array in instructions)
var table = [1,2,3,4,5,6,7,8,9,10];
console.log(table);

/*------------------------------------------Variables---------------------------------------------*/
var fiveTable = [], tenTable = [], squaresTable = [], table2 = [];
var evenTable = [], oddTable = [], extraCredit = [];
var i, sum, sum2, odd, bonus3, volume;

// Per email we can loop to create array of elements 1 - 100 for question 3 & 4
for(i = 0; i < 100; i++){table2[i] = i + 1;}

/*------------------------------------------Part 2------------------------------------------------*/
//a. All multiples of 5 created from each element of table
table.map(function(x, i){fiveTable[i] = 5 * x;});
//b. All multiples of 10 created from each element of table
table.map(function(x, i){tenTable[i] = 10 * x;});
//c. All squares of the elements of table
table.map(function(x, i){squaresTable[i] = x * x;});
console.log(fiveTable);
console.log(tenTable);
console.log(squaresTable);

/*------------------------------------------Part 3------------------------------------------------*/
// Filter out the odd multiples of 5 from elements of table2
oddTable = table2.filter(function(x){return x % 2 != 0 && x % 5 === 0;});
console.log(oddTable);

/*------------------------------------------Part 4------------------------------------------------*/
// Filter out the even multiples of 7 from elements of table2
evenTable = table2.filter(function(x){return x % 2 === 0 && x % 7 === 0;});
// Reduce table2 to the sum of the elements filtered 
sum = evenTable.reduce(function(a,b){return a + b})
console.log(sum);
/*-------------------------------------------Part 5----------------------------------------------*/
// Take in one var & wait, execute internal function call
volume = function(r){
	return function(h){console.log(3.14 * r * r * h);};
};
cylinder = volume(5);
cylinder(10);

/*------------------------------------------Bonus Part 3---------------------------------------------*/
// Used currying to take in the even (0) or odd (1) term first then the multiple number
bonus3 = function(x){
	if(x){
		return function(y){
			extraCredit = table2.filter(function(data){return data % 2 != 0 && data % y === 0;});
		};
	}
	else{
		return function(y){
			extraCredit = table2.filter(function(data){return data % 2 === 0 && data % y === 0;});
		};
	}
};
// Let 0 = even and 1 = odd
odd = bonus3(0);
odd(7);
// Reduce the array to the sum of its elements
sum2 = extraCredit.reduce(function(a,b){return a + b})
console.log(extraCredit);
console.log(sum2);
