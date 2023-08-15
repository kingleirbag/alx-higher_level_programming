#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let cross = '';
      for (let j = 0; j < this.width; j++) {
        cross += 'X';
      }
      console.log(cross);
    }
  }

  rotate () {
    const widthStored = this.width;
    this.width = this.height;
    this.height = widthStored;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
