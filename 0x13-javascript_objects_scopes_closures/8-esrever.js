#!/usr/bin/node
exports.esrever = function (list) {
  let listLength = list.length - 1;
  let count = 0;
  while ((listLength - count) > 0) {
    const aux = list[listLength];
    list[listLength] = list[count];
    list[count] = aux;
    count++;
    listLength--;
  }
  return list;
};
