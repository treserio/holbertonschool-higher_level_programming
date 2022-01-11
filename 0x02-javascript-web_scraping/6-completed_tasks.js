#!/usr/bin/node
const req = require('request');

req.get(process.argv[2], (e, r) => {
  const tdCnt = {};
  for (const todo of JSON.parse(r.body)) {
    if (todo.completed) {
      if (!(todo.userId in tdCnt)) {
        tdCnt[todo.userId] = 1;
      } else {
        ++tdCnt[todo.userId];
      }
    }
  }
  console.log(tdCnt);
});
