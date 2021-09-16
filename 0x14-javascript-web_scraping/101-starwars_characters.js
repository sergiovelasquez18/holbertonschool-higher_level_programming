#!/usr/bin/node
// script that computes the number of tasks completed by user id
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const j = JSON.parse(body);
    for (let i = 0; i < j.characters.length; i++) {
      const newurl = j.characters[i];
      request(newurl, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const h = JSON.parse(body);
          console.log(h.name);
        }
      });
    }
  }
});
