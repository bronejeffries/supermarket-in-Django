function removerow(id){

  var rmv = id.parentElement;
  var child = rmv.parentElement;
  var parent = child.parentElement;
  var table = parent.parentElement;
  table.removeChild(parent);
}

function strikethrough(id){
  var tr = id.parentElement.parentElement.parentElement.parentElement;

  var column = tr.getElementsByTagName('td')[1];
  console.log(column);
}


function showaddEmployee(){
  document.getElementById('addEmployee').style.display="block";
}

function closeadd(id){
  // var rmve = id.parentElement;
  // var child = rmve.parentElement;
  // var parent = child.parentElement;
  id.parentElement.parentElement.parentElement.style.display="none";
}

// Create a "close" button and append it to each list item
var list = document.getElementsByClassName('todo_list')[0];
var myNodelist = list.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
  myNodelist[i].addEventListener('click',function (ev) {
      ev.target.classList.toggle('checked');
  });
}

// Click on a close button to hide the current list item
var close = list.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}

// Add a "checked" symbol when clicking on a list item
// var listul = document.querySelector('ul');
// listul.addEventListener('click', function(ev) {
//   if (ev.target.tagName === 'LI') {
//     ev.target.classList.toggle('checked');
//   }
// }, false);
