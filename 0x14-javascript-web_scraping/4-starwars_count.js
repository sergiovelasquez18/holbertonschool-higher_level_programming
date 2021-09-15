#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];
let resulDict = {};
let count = 0;
let i = 0;
let j = 0;
request(url, function (
  error, response, body) {
  if (error) {
    console.log(error);
  } else {
    resulDict = JSON.parse(body);
    for (i = 0; i < resulDict.results.length; i++) {
      for (j = 0; j < resulDict.results[i].characters.length; j++) {
        if (resulDict.results[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
