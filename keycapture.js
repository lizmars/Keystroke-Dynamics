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

  s = timelog[0]/1000.0;
  for(i = 0; i < timelog.length; i++ ){
    timelog[i] = (timelog[i]/1000.0) - s;
  }
  timelog.toString()


  var parameters = '{ "' + username + '" : [' +
  '{ "Keys":"'+ keylog + '" , "Times":"' + timelog +'" }]}';

      $.ajax({
          url: 'http://127.0.0.1:8080',
          headers: {
              'Type':'Create_Profile',
              'User':username,
              'Content-Type':'application/json'
          },
          method: 'POST',
          //dataType: 'json',
          data: parameters,
          success: function(result){
            document.getElementById("sub").disabled = true;
            document.getElementById("keysrec").value = "";
            if (result == "True") {
               document.getElementById("CPEnd").style.display = "block"
            }
            else {
              document.getElementById("CPError").style.display = "block"
            }


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

function checkname(){
 var name=document.getElementById( "userID" ).value;

 if(name){
   $.ajax({
       url: 'http://127.0.0.1:8080',
       headers: {
           'Type':'is_in_DB',
           'User': name,
       },
       method: 'POST',
       dataType: 'text',
       success: function(response){
         //window.alert(response)
         document.getElementById("name_status").style.display = "block"
         if (response == "OK"){
           document.getElementById("name_status").style.color = "green"
           document.getElementById("name_status").innerHTML = "Good Username";
           document.getElementById("nexstep").disabled = false;
         }
         else {
           document.getElementById("name_status").style.color = "red"
           document.getElementById("name_status").innerHTML = response;
           document.getElementById("nexstep").disabled = true;
         }

       }
     });
 }
 else{
  $( '#name_status' ).html("");
  return false;
 }

}

function checknameA(){
 var name=document.getElementById( "userIDauth" ).value;

 if(name){
   $.ajax({
       url: 'http://127.0.0.1:8080',
       headers: {
           'Type':'is_in_DB',
           'User': name,
       },
       method: 'POST',
       dataType: 'text',
       success: function(response){
         //window.alert(response)
         document.getElementById("name_status_Auth").style.display = "block"
         if (response == "OK"){
           document.getElementById("name_status_Auth").style.color = "red"
           document.getElementById("name_status_Auth").innerHTML = "Username is not found. Please enter valid User Name";
           document.getElementById("nextstep").disabled = true;
         }
         else {
           document.getElementById("name_status_Auth").style.color = "green"
           document.getElementById("name_status_Auth").innerHTML = "Username Exist";
           document.getElementById("nextstep").disabled = false;
         }

       }
     });
 }
 else{
  $( '#name_status' ).html("");
  return false;
 }

}
