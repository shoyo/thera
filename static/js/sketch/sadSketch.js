function sadSet(){
  count = 5;
  ripples = new Array(count);
  for (var i=0;i<ripples.length;i++){
    ripples[i] = new Ripple(random(0,width), random(0,height), 250, 1, 0, 2);
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
