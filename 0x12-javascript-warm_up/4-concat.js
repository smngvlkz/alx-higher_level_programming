#!/usr/bin/node

function printArgs(arg1, arg2) {
  console.log(`${arg1} is ${arg2}`);
}

const args = process.argv.slice(2);
printArgs(args[0], args[1]);
