#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (err, res, body) {
  if (!err) {
    const content = JSON.parse(body).results;
    console.log(content.reduce((count, film) => {
      return film.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
