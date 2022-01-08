#!/usr/bin/node
const Sq = require('./5-square');

module.exports = class Square extends Sq {
  constructor(size) {
    super(size, size);
  }

  charPrint(c) {
    if (c) {
      for (let i = 0; i < this.height; ++i) {
        console.log(c.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.height; ++i) {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
