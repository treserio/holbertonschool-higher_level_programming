#!/usr/bin/node
const n = process.argv[2];

if (parseInt(n) || n === '0') {
  for (let i = n; i > 0; i--) {
    console.log('X'.repeat(n));
  }
} else {
  console.log('Missing size');
}
