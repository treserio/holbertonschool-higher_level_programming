#!/usr/bin/node
const num = parseInt(process.argv[2]);

for (i = 1; i; --i)
  console.log("C is fun\n".repeat(num - 1) + "C is fun");
