#!/usr/bin/node
const req = require('request');
req.get(process.argv[2]).on('response', (r) => {
  console.log('code: ' + r.statusCode);
});
