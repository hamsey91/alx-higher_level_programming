#!/usr/bin/node
const { readFileSync, writeFile } = require('fs');
const { argv } = require('process');

const readContent = (file) => {
  return readFileSync(file, 'utf8');
};

const concatFiles = readContent(argv[2]) + '' + readContent(argv[3]);

writeFile(argv[4], concatFiles, 'utf8', err => {
  if (err) throw err;
});
