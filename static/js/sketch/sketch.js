var animation = true;

var width;
var height;

var r = 0;
var cl = 0;
var mood = 'land';

var ripples = [];
var sparks = [];
var particles = [];
var flowField;

function setup() {
  updateWindowSize();
  var myCanvas = createCanvas(width, height);
  myCanvas.class('backgroundsketch '+mood);
  // document.getElementById(defaultCanvas0).classList.add('happiness');

  // document.getElementById('name').innerHTML = mood.charAt(0).toUpperCase() + mood.slice(1);
    switch(mood){
      case 'land' :
        landingSet();
        break;

      case 'happiness' :
        happySet();
        break;

      case 'sadness' :
        sadSet();
        break;
    }
}

function draw(){
  cl++;
  if(animation){
    document.getElementById('fps').innerHTML = ': ' + floor(getFrameRate()) + 'fps';
    switch(mood){
      case 'land' :
        landingDraw(cl);
        break;

      case 'happiness' :
        happyDraw(cl);
        break;

      case 'sadness' :
        sadDraw(cl);
        break;
    }
  }
}

function keyPressed() {
  if (keyCode === UP_ARROW) {
    if (animation) {
      animation = false;
    } else {
      animation = true;
    }
  }

  if (keyCode === DOWN_ARROW) {
    if (animation) {
      if(document.getElementById('fps').style.display === 'none'){
        document.getElementById('fps').style.display = 'block';
      } else {
        document.getElementById('fps').style.display = 'none';
      }
    }
  }

  return false; // prevent default
}

function windowResized() {
  updateWindowSize()
  resizeCanvas(width, height);
}

function updateWindowSize(){
  // width = window.innerWidth;
  // height = window.innerHeight;

  width = Math.max(
    // document.body.scrollWidth, document.documentElement.scrollWidth,
    document.body.offsetWidth, document.documentElement.offsetWidth,
    document.body.clientWidth, document.documentElement.clientWidth
  );
  height = Math.max(
    document.body.scrollHeight, document.documentElement.scrollHeight,
    document.body.offsetHeight, document.documentElement.offsetHeight,
    document.body.clientHeight, document.documentElement.clientHeight
  );
}
