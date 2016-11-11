var keylog = [];
var timelog = [];
var username
openTab("Home")
function openTab(tabName) {
    var i;
    var x = document.getElementsByClassName("tab");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";
    }
    document.getElementById(tabName).style.display = "block";
}
function keydown(){
  keylog.push(event.keyCode + "1");
  timelog.push(event.timeStamp);
}

function keyup(){
  keylog.push(event.keyCode + "0");
  timelog.push(event.timeStamp);
}

function submit() {
  username = document.getElementById("userID").value
  keylog.toString();
  document.getElementById("out_keys").innerHTML = keylog;
  s = timelog[0]/1000.0
  for(i = 0; i < timelog.length; i++ ){
    timelog[i] = (timelog[i]/1000.0) - s
  }
  timelog.toString()
  document.getElementById("out_times").innerHTML = timelog;
  document.getElementById("out_user").innerHTML = username;

  var parameters = '{ "' + username + '" : [' +
  '{ "Keys":"'+ keylog + '" , "Times":"' + timelog +'" }]}';

  $(document).ready(function(){
          $.post("http://127.0.0.1:8080",
          parameters,
          function(data,status){
              alert("Data: " + data + "\nStatus: " + status);
          }, "json");
      });
}
