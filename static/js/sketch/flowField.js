function FlowField(scl,rng) {
  if(scl>0) {
    this.scl = height/scl;
  } else {
    this.scl = height/40;
  }
  this.range = rng;
  this.inc = 0.1;
  this.c = floor(width / this.scl);
  this.r = floor(height / this.scl);
  this.field = new Array(this.r*this.c);
  this.zoff = 0;
}

FlowField.prototype.update = function(){
  this.scl = (height)/40;
  var yoff = 0;
  for (var y = 0; y < this.r; y++) {
    var xoff = 0;
    for (var x = 0; x < this.c; x++) {
      var ind = x + y * this.c;
      var angle = noise(xoff, yoff, this.zoff) * TWO_PI * this.range;
      var v = p5.Vector.fromAngle(angle);
      v.setMag(1);
      flowField[ind] = v;
      xoff += this.inc;
    }
    yoff += this.inc;
    this.zoff += 0.0004;
  }
}
