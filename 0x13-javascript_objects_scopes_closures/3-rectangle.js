#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  function print() {
    const i = 0;
    const x = 0;

    while (i < this.width) {
      while (x < this.height) {
        console.log(`X`);
        x++;
      }
      i++;
}

module.exports = Rectangle;
