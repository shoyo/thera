function Ripple(x,y,s,v,t,l){
  this.pos = createVector(x,y);
  this.size = s;
  this.vel = v;
  this.t = t;
  this.numOfLayers = l;
  this.alpha = 0;
}

Ripple.prototype.drop = function() {
  this.t++;
  if (this.alpha<0.01){
    // console.log(this.alpha);
    this.reset();
  }

  noFill();
  strokeWeight(2);

  this.alpha = 0.3*(this.size-this.vel*this.t)/this.size;
  c = color('rgba(255, 255, 255, '+this.alpha+')');
  stroke(c);
  for (l = 0; l<this.numOfLayers; l++){
    r=pow(1.6,l)*this.vel*this.t;
    this.rip(r);
  }

};

Ripple.prototype.rip = function(r) {
  ellipse(this.pos.x, this.pos.y, r, r);
};

Ripple.prototype.reset = function() {
  // console.log('reset drop');
  this.alpha = 0;
  this.pos.x = random(0,width);
  this.pos.y = random(0,height);
  this.size = random(150,250);
  this.vel = 1;
  this.t = 0;
  if(this.size<200){
    this.numOfLayers = 2;
  }else{
    this.numOfLayers = 3;
  }
};
