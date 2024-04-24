#!/usr/bin/node

const req = require('request');
const Id = process.argv[2];
const Url = `https://swapi-api.alx-tools.com/api/films/${Id}`;

req.get(Url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const actors = data.characters;
    for (const actor of actors) {
      req.get(actor, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          const identity = JSON.parse(body);
          console.log(identity.name);
        }
      });
    }
  }
});
