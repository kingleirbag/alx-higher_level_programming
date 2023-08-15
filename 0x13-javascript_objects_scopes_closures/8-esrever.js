#!/usr/bin/node
exports.esrever = function (list) {
  let list_length = list.length - 1;
  let count = 0;
  while ((list_length - count) > 0) {
    const aux = list[list_length];
    list[list_length] = list[count];
    list[count] = aux;
    count++;
    list_length--;
  }
  return list;
};
