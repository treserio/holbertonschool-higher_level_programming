#!/usr/bin/node
exports.esrever = function (list) {
  const rez = [];
  for (let i = list.length - 1; i >= 0; --i) {
    rez.push(list[i]);
  }
  return rez;
};
