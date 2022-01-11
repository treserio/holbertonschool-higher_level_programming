#!/usr/bin/node
const req = require('request');
const fs = require('fs');
req.get(process.argv[2], (e, r) => {
  fs.writeFileSync(process.argv[3], r.body, 'utf8');
});
