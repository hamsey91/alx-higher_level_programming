#!/usr/bin/node

const req = require('request');

req.get(process.argv[2], { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const cmptsk = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!cmptsk[todo.userId]) {
        cmptsk[todo.userId] = 1;
      } else {
        cmptsk[todo.userId] += 1;
      }
    }
  });
  console.log(cmptsk);
});
