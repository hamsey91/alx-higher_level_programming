#!/usr/bin/node

const req = require('request');
const Id = process.argv[2];
const Url = `https://swapi-api.alx-tools.com/api/films/${Id}`;

req(Url, function (err, res, body) {
    if (!err) {
      const actors = JSON.parse(body).characters;
      printallcharacters(actors, 0);
    }
  });
  
function printallcharacters (actors, count) {
    req(actors[count], function (err, res, body) {
      if (!err) {
        console.log(JSON.parse(body).name);
        if (count + 1 < actors.length) {
            printallcharacters(actors, count + 1);
        }
      }
    });
}
