#!/usr/bin/node
const req = require('request');

req.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (e, r) => {
  const chars = JSON.parse(r.body).characters;
  const allPeeps = [];
  req.get('https://swapi-api.hbtn.io/api/people/', (er, res) => {
    allPeeps.push(...JSON.parse(res.body).results);
    for (let i = 2; i < 10; ++i) {
      req.get('https://swapi-api.hbtn.io/api/people/?page=' + i, (er, res2) => {
        allPeeps.push(...JSON.parse(res2.body).results);
      });
    }
    setTimeout(() => {
      for (const chUrl of chars) {
        for (const chInfo of allPeeps) {
          if (chInfo.url == chUrl) {
            console.log(chInfo.name);
          }
        }
      }
    }, 3000);
  });
})
