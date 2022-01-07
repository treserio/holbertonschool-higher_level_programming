#!/usr/bin/node
const n = process.argv[2];

if (parseInt(n) || n === '0') {
  for (let i = n; i > 0; i--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
