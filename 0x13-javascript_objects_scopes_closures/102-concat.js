#!/usr/bin/node
const fs = require('fs');

const first_Arg = fs.readFileSync(process.argv[2]).toString();
const second_Arg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], first_Arg + second_Arg);
