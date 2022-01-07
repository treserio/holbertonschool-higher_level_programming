#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const data = process.argv.slice(2);
  console.log(data.sort((a, b) => b - a)[1]);
}
