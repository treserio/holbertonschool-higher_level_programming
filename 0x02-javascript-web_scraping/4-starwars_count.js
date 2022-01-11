#!/usr/bin/node
const req = require('request');
req.get(process.argv[2], (e, r) => {
  let cnt = 0;
  for (const movie of JSON.parse(r.body).results) {
    for (const char of movie.characters) {
      if (char.split('/').slice(-2, -1)[0] === '18') {
        ++cnt;
      }
    }
  }
  console.log(cnt);
});
