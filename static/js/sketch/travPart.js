function TravPart(c){
  this.pos = createVector(random(width), random(height));
  this.vel = createVector(0, 0);
  this.acc = createVector(0, 0);
  this.maxvel = 7;
  this.prevPos = this.pos.copy();
  this.color = c;
}

TravPart.prototype.flow = function(field) {
  var x = floor(this.pos.x / field.scl);
  var y = floor(this.pos.y / field.scl);
  var ind = x + y * field.c;
  var force = field[ind];
  this.force(force);
};

TravPart.prototype.force = function(force) {
  this.acc.add(force);
};

TravPart.prototype.update = function() {
  this.vel.add(this.acc); //Accelerate
  this.vel.limit(this.maxvel); //Limit speed
  this.pos.add(this.vel); //Move
  this.acc.mult(0);
};

TravPart.prototype.updatePrevious = function() {
  this.prevPos.x = this.pos.x;
  this.prevPos.y = this.pos.y;
};

TravPart.prototype.edges = function() {
  if (this.pos.x < 0) {
    this.pos.x = width;
    this.updatePrevious();
  }
  if (this.pos.x > width) {
    this.pos.x = 0;
    this.updatePrevious();
  }
  if (this.pos.y < 0) {
    this.pos.y = height;
    this.updatePrevious();
  }
  if (this.pos.y > height) {
    this.pos.y = 0;
    this.updatePrevious();
  }
};

TravPart.prototype.show = function(intensity) {
  // intensity = random(0,height/40);
  // stroke(255, random(240,255), random(205,255), 50);
  // stroke(255, 220, 205, 25);
  stroke(this.color);
  strokeWeight(intensity);
  line(this.pos.x, this.pos.y, this.prevPos.x, this.prevPos.y);
  this.updatePrevious();
};

TravPart.prototype.deploy = function(intensity) {
  this.flow(flowField);
  this.update();
  this.edges();
  this.show(intensity);
};
