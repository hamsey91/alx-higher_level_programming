#!/usr/bin/node

const filesys = require('fs');
const req = require('request');

req(process.argv[2]).pipe(flesys.createWriteStream(process.argv[3]));
