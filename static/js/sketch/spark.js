function Spark(x,y,s,l,v,t,spkMin,spkMax){
  this.pos = createVector(x,y);
  this.size = s;
  this.len = l
  this.vel = v;
  this.t = t;
  this.numOfSparks = spkMin;
  this.minSparks = spkMin;
  this.maxSparks = spkMax;
  this.avSparks = floor((this.minSparks+this.maxSparks)/2);
  this.alpha = 0;
}

Spark.prototype.light = function() {
  this.t++;
  if (this.alpha<0.01){
    // console.log(this.alpha);
    this.reset();
  }

  noFill();
  strokeWeight(2);

  this.alpha = (this.size-this.vel*this.t)/this.size;
  var c = color('rgba(255, 255, 255, '+this.alpha+')');
  stroke(c);
  for (var n = 0; n<this.numOfSparks; n++){
    var r=this.vel*this.t;
    this.jump(r,n*TWO_PI/this.numOfSparks);
  }

};

Spark.prototype.jump = function(r,theta) {
  // fill(255,255,255);
  // circle(this.pos.x+r*cos(theta),this.pos.y+r*sin(theta),5);
  strokeWeight(7);
  line(this.pos.x+r*cos(theta), this.pos.y+r*sin(theta), this.pos.x+(r-this.len)*cos(theta), this.pos.y+(r-this.len)*sin(theta));
};


// Bad design to have a reset set hard values
Spark.prototype.reset = function() {
  // console.log('reset velop');
  this.alpha = 0;
  this.pos.x = random(0,width);
  this.pos.y = random(0,height);
  this.size = random(100,200);
  this.t = 0;
  if(this.size<150){
    this.numOfSparks = random(this.minSparks,this.avSparks);
  }else{
    this.numOfSparks = random(this.avSparks,this.maxSparks);
  }
};
