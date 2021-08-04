#!/usr/bin/node
// script that computes and prints a factorial
function factorialRe(n) {
	if (!n){
		return 1;
	} else {
    return n * factorialRe (n - 1);
  }
}

console.log(factorialRe(parseInt(process.argv[2])));