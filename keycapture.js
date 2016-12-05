var keylog = [];
var timelog = [];
var username;

function keydown(){
  keylog.push(event.keyCode + "1");
  timelog.push(event.timeStamp);
}

function keyup(){
  keylog.push(event.keyCode + "0");
  timelog.push(event.timeStamp);
}

function keydownAuth(){
  keylog.push(event.keyCode + "1");
  timelog.push(event.timeStamp);
  if ((keylog.length%150 == 0) && (timelog.length%150 == 0)){
    auth();
  }

}

function keyupAuth(){
  keylog.push(event.keyCode + "0");
  timelog.push(event.timeStamp);
  if ((keylog.length%150 == 0) && (timelog.length%150 == 0)){
    auth();
  }
}


function submit() {
  username = document.getElementById("userID").value;
  keylog.toString();
  document.getElementById("out_keys").innerHTML = keylog;
  s = timelog[0]/1000.0;
  for(i = 0; i < timelog.length; i++ ){
    timelog[i] = (timelog[i]/1000.0) - s;
  }
  timelog.toString()
  document.getElementById("out_times").innerHTML = timelog;
  document.getElementById("out_user").innerHTML = username;

  var parameters = '{ "' + username + '" : [' +
  '{ "Keys":"'+ keylog + '" , "Times":"' + timelog +'" }]}';

  /*$(document).ready(function(){
          $.post("http://127.0.0.1:8080",
          parameters,
          function(data,status){
              alert("Data: " + data + "\nStatus: " + status);
          }, "json");
      });*/
      $.ajax({
          url: 'http://127.0.0.1:8080',
          headers: {
              'Type':'Create_Profile',
              'User':username,
              'Content-Type':'application/json'
          },
          method: 'POST',
          dataType: 'json',
          data: parameters,
          success: function(data){
            console.log('succes: '+data);
          }
        });
  keylog = [];
  timelog = [];
}

function auth(){
  username = document.getElementById("userIDauth").value;
  keylog.toString();
  document.getElementById("out_keys").innerHTML = keylog;
  s = timelog[0]/1000.0;
  for(i = 0; i < timelog.length; i++ ){
    timelog[i] = (timelog[i]/1000.0) - s;
  }
  timelog.toString();
  document.getElementById("out_times").innerHTML = timelog;
  document.getElementById("out_user").innerHTML = username;

  param = '{ "' + username + '" : [' +
  '{ "Keys":"'+ keylog + '" , "Times":"' + timelog +'" }]}';
  $.ajax({
      url: 'http://127.0.0.1:8080',
      headers: {
          'Type':'Auth',
          'User':username,
          'Content-Type':'application/json'
      },
      method: 'POST',
      dataType: 'json',
      data: param,
      success: function(data){
        console.log('succes: '+data);
      }
    });
  delete param;

}
