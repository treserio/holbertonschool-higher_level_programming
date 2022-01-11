#!/usr/bin/node
const req = require('request');
req.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (e, r) => {
  console.log(JSON.parse(r.body).title);
});
