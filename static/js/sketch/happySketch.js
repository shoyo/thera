function happySet(){
  flowField = new FlowField();
  for (var i = 0; i < 50; i++) {
    particles[i] = new TravPart();
  }

  sparkCount = 2;
  sparks = new Array(sparkCount);
  for (var i=0;i<sparks.length;i++){
    sparks[i] = new Spark(random(0,width), random(0,height), 75, 20, 5, 0, 3, 4);
    console.log(sparks[i]);
  }

  rippleCount = 10;
  ripples = new Array(rippleCount);
  for (var i=0;i<ripples.length;i++){
    if(i<floor(ripples.length/2)){
      var rippleClr = color(random(32, 63),random(127,190),random(127,255),255);
    }else{
      var rippleClr = color(random(190, 255),0,random(63,127),255);
    }
    ripples[i] = new Ripple(random(0,width), random(0,height), 100, 1, 10, 1/2, 0, 1, 1, rippleClr);
    console.log(ripples[i]);
  }

}

function happyDraw(t){
  clear();

  flowField.update();
  for (var i = 0; i < particles.length; i++) {
    particles[i].deploy();
  }

  for (var i=0;i<sparkCount;i++){
    sparks[i].light();
  }
  blendMode(MULTIPLY);
  for (i=0;i<rippleCount;i++){
    ripples[i].drop();
  }
  blendMode(NORMAL);

}
