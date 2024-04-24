#!/usr/bin/node
const req = require('request');
const Url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

req(Url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const content = JSON.parse(body);
    console.log(content.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
