function Ripple(x,y,s,wmin,wmax,v,t,lmin,lmax,clr){
  this.pos = createVector(x,y);
  this.size = s;
  this.avSize = s;
  this.weight = wmin;
  this.weightMin = wmin;
  this.weightMax = wmax;
  this.vel = v;
  this.t = t;
  this.numOfLayers = lmin;
  this.minLayers = lmin;
  this.maxLayers = lmax;
  this.alpha = 0;
  this.color = clr;
}

Ripple.prototype.drop = function() {
  this.t++;
  if (this.alpha<0.01){
    // console.log(this.alpha);
    this.reset();
  }

  noFill();
  strokeWeight(this.weight);
  // console.log(this.weightMin+' : '+this.weightMax+' -> '+this.weight);

  this.alpha = alpha(this.color)/255*(this.size-this.vel*this.t)/this.size;
  var c = color(red(this.color),green(this.color),blue(this.color),255*this.alpha);
  console.log(c, this.alpha);
  stroke(c);
  for (var l = 0; l<this.numOfLayers; l++){
    var r=pow(1.6,l)*this.vel*this.t;
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
  this.t = 0;
  this.size = random(3*this.size/4,5*this.size/4);
  this.weight = random(this.weightMin,this.weightMax);
  if(this.size<this.avSize){
    this.numOfLayers = this.minLayers;
  }else{
    this.numOfLayers = this.maxLayers;
  }
};
