#!/usr/bin/node
// prints an argument that can be converted to a number to an integer
if (!parseInt(process.argv[2])) { // parseInt: conviert de str to int
  console.log('Not a number');
} else {
  console.log('My number: %d', parseInt(process.argv[2]));
}
