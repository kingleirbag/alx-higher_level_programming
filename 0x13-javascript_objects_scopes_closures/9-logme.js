#!/usr/bin/node
let argumnt = 0;

exports.logMe = function (item) {
  console.log(argumnt + ': ' + item);
  argumnt++;
};
