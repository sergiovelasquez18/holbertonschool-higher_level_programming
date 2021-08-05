#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  const array = process.argv.sort((a, b) => a - b);
  const length = array.length;

  console.log(array[length - 2]);
}
