function landingSet(){
  flowField = new FlowField(0,3);
  var c = color(255, 220, 205, 25);
  for (var i = 0; i < 500; i++) {
    particles[i] = new TravPart(c);
  }

  count = 1;
  sparks = new Array(count);
  for (var i=0;i<sparks.length;i++){
    sparks[i] = new Spark(random(0,width), random(0,height), 200, 15, 3, 0, 3, 6);
    console.log(sparks[i]);
  }

}

function landingDraw(t){
  clear();

  flowField.update();
  for (var i = 0; i < particles.length; i++) {
    particles[i].deploy(random(0,height/40));
  }

  for (var i=0;i<count;i++){
    sparks[i].light();
  }

}
