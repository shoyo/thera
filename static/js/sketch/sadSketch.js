function sadSet(){
  flowField = new FlowField(30,1/2);
  var c = color(255,255,255,15);
  for (var i = 0; i < 20; i++) {
    particles[i] = new TravPart(c);
  }

  count = 5;
  ripples = new Array(count);
  var clr = color(255,255,255,95);
  for (var i=0;i<ripples.length;i++){
    ripples[i] = new Ripple(random(0,width), random(0,height), 250, 2, 2, 1, 0, 2, 3, clr);
    console.log(ripples[i]);
  }
}

function sadDraw(t){
  clear();
  flowField.update();
  for (var i = 0; i < particles.length; i++) {
    particles[i].deploy(random(0,height/20));
  }

  for (i=0;i<count;i++){
    ripples[i].drop();
  }
  // console.log('Drop: '+t);
}
