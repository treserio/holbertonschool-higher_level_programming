#!/usr/bin/node
const req = require('request');
let cnt = 0;
req.get('https://swapi-api.hbtn.io/api/films/', (e, r) => {
  for (movie of JSON.parse(r.body).results) {
    for (char of movie.characters) {
      if (char.split('/').slice(-2, -1) == process.argv[2]) {
        ++cnt;
      }
    }
  }
  console.log(cnt);
});
