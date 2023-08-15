#!/usr/bin/node
const dict_obj = require('./101-data').dict;

const total_entries = Object.entries(dict_obj);
const dict_vals = Object.values(dict_obj);
const valsUniq = [...new Set(dict_vals)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in totalist) {
    if (total_entries[k][1] === valsUniq[j]) {
      list.unshift(total_entries[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
