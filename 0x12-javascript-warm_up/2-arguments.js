#!/usr/bin/node
const number = process.argv.length - 2;

if (number === 0) {
  console.log('No argument');
} else if (number === 1) {
  console.log('Argumrnt found');
} else {
  console.log('Arguments found');
}
