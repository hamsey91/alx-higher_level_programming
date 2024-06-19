#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let elem = 0;
  while ((len - elem) > 0) {
    const temp = list[len];
    list[len] = list[elem];
    list[elem] = temp;
    elem++;
    len--;
  }
  return list;
};
