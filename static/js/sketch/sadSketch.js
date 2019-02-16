function sadSet(){
  count = 5;
  ripples = new Array(count);
  var clr = color(255,255,255,77);
  for (var i=0;i<ripples.length;i++){
    ripples[i] = new Ripple(random(0,width), random(0,height), 250, 2, 2, 1, 0, 2, 3, clr);
    console.log(ripples[i]);
  }
}

function sadDraw(t){
  clear();
  for (i=0;i<count;i++){
    ripples[i].drop();
  }
  // console.log('Drop: '+t);
}
