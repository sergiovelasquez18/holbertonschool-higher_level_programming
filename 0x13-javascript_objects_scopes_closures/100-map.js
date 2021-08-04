#!/usr/bin/node
// script that imports an array and computes a new array

const list = require('./100-data.js').list;
console.log(list);
const map1 = list.map((x, i) => { return x * i; });
console.log(map1);
