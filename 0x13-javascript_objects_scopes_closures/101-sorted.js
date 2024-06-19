#!/usr/bin/node
const { dict } = require('./101-data');
const NewEntries = Object.entries(dict);
const nObject = {};

NewEntries.forEach(elem => {
  nObject[elem[1]] ? nObject[elem[1]].push(elem[0]) : nObject[elem[1]] = [elem[0]];
});

console.log(nObject);
