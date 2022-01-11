#!/usr/bin/node
const req = require('request');
let cnt = 0;
req.get('https://swapi-api.hbtn.io/api/films/', (e, r) => {
  for (const movie of JSON.parse(r.body).results) {
    for (const char of movie.characters) {
      if (char.split('/').slice(-2, -1)[0] === process.argv[2]) {
        ++cnt;
      }
    }
  }
  console.log(cnt);
});
