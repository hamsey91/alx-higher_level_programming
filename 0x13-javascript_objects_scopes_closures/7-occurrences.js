#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let elem = 0; elem < list.length; elem++) {
    if (searchElement === list[elem]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
