#!/usr/bin/node
const req = require('request');
req.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (e, r) => {
  for (const char of JSON.parse(r.body).characters) {
    req.get(char, (er, rq) => {
      console.log(JSON.parse(rq.body).name);
    });
  }
});
