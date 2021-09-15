#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(process.argv[3], body, (error) => {
    if (error) {
      console.log('code:', response && response.statusCode);
    }
  });
});
