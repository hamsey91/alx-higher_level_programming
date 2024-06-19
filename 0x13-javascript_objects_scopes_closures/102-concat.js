#!/usr/bin/node
const { readFile, writeFile } = require('fs');
const { argv } = require('process');

const readContent = (file) => {
  return readFile(file, 'utf8');
};
const concatFiles = readContent(argv[2]) + '' + readContent(argv[3]);
writeFile(argv[4], concatFiles, 'utf8', err => {
  if (err) throw err;
});
