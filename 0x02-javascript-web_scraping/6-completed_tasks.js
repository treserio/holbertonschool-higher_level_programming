#!/usr/bin/node
const req = require('request');

req.get(process.argv[2], (e, r) => {
  let td_cnt = {};
  for (const todo of JSON.parse(r.body)) {
    if (todo.completed) {
      if (!(todo.userId in td_cnt)) {
        td_cnt[todo.userId] = 1;
      } else {
        ++td_cnt[todo.userId];
      }
    }
  }
  console.log(td_cnt);
});
