#!/usr/bin/node
exports.converter = function (base) {
  return (B2) => B2.toString(base);
};
