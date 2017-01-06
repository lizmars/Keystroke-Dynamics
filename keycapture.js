var keylog = [];
var timelog = [];
var username;

function move(){
  if (keylog.length <= 770) {
    var width = keylog.length;
    document.getElementById("Bar").style.width = width +  'px';
  }
  else{
    document.getElementById("alert").style.display = "block";
  }
}

function keydown(){
  if (document.getElementById("sub").disabled){
    document.getElementById("sub").disabled = false
  }
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
  if ((keylog.length%40 == 0) && (timelog.length%40 == 0)){
    auth();
  }

}

function keyupAuth(){
  keylog.push(event.keyCode + "0");
  timelog.push(event.timeStamp);
  if ((keylog.length%40 == 0) && (timelog.length%40 == 0)){
    auth();
  }
}


function submit() {
  username = $("#placehold").text();
  //document.getElementById("sub").disabled = true

  if (document.getElementById("keysrec").value.length != 0){ //if text area is not empty start process

    keylog.toString();
    s = timelog[0]/1000.0;
    for(i = 0; i < timelog.length; i++ ){
      timelog[i] = (timelog[i]/1000.0) - s;
    }
    timelog.toString()
    var parameters = '{ "' + username + '" : [' +
    '{ "Keys":"'+ keylog + '" , "Times":"' + timelog +'" }]}';

        $.ajax({
            url: 'http://107.170.249.133:8000',
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
                 document.getElementById("beginauth").focus();
                 document.getElementById("sub").disabled = true
              }
              else {
                document.getElementById("CPError").style.display = "block"
              }
            }
          });
    keylog = [];
    timelog = [];

    document.getElementById("keysrec").value = "";
    document.getElementById("Bar").style.width = 1 + "px";
    document.getElementById("placehold").value = "";
  }
  else {
    alert("Enter some text first") //if texarea is empty
  }
}

function auth(){
  username = $("#placehld").text();

  keylog.toString();
  //document.getElementById("out_keys").innerHTML = keylog;
  s = timelog[0]/1000.0;
  for(i = 0; i < timelog.length; i++ ){
    timelog[i] = (timelog[i]/1000.0) - s;
  }
  timelog.toString();
  //document.getElementById("out_times").innerHTML = timelog;
  //document.getElementById("out_user").innerHTML = username;

  param = '{ "' + username + '" : [' +
  '{ "Keys":"'+ keylog + '" , "Times":"' + timelog +'" }]}';
  $.ajax({
      url: 'http://107.170.249.133:8000',
      headers: {
          'Type':'Auth',
          'User':username,
          'Content-Type':'application/json'
      },
      method: 'POST',
      data: param,
      success: function(result){

        document.getElementById("result").style.display = "block"
        if (result == "Wait") {
          document.getElementById("result").style.color = "blue"
        }
        var res = result.split(" ")
        //document.getElementById("result").innerHTML = res[1]
        switch (res[1]) {
          case "Permitted:":
            document.getElementById("result").style.color = "green"
            break;
          case "Denied:":
            document.getElementById("result").style.color = "red"
            break;

        }

          document.getElementById("result").innerHTML = result
      }
    });
  delete param;

}

function checkname(){
 var name=document.getElementById( "userID" ).value;
 if (document.getElementById( "userID" ).value.length == 0){
   document.getElementById("nexstep").disabled = true;
 }


 if(name){
   $.ajax({
       url: 'http://107.170.249.133:8000',
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
 if (document.getElementById( "userIDauth" ).value.length == 0){
   document.getElementById("nextstep").disabled = true;
 }

 if(name){
   $.ajax({
       url: 'http://107.170.249.133:8000',
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

function clearContent(){
  if (username != $("#placehold").text()){
    keylog = [];
    timelog = [];
    document.getElementById("Bar").style.width = 1 + "px"
  }
  if (document.getElementById("userID").value.length != 0 ) {
    document.getElementById("placehold").innerHTML = document.getElementById("userID").value
    document.getElementById("userID").value = ""
    document.getElementById("name_status").style.display = "none"
    document.getElementById("nexstep").disabled = true
  }
  if (document.getElementById("keysrec").value.length != 0 ) {
    document.getElementById("keysrec").value = ""
  }
  if (document.getElementById("keyrec").value.length != 0 ) {
    document.getElementById("keyrec").value = ""
    document.getElementById("result").style.display = "none"
  }

  if (document.getElementById("userIDauth").value.length != 0 ) {
    document.getElementById("placehld").innerHTML = document.getElementById("userIDauth").value
    document.getElementById("userIDauth").value = ""
    document.getElementById("name_status_Auth").style.display = "none"
    document.getElementById("nextstep").disabled = true
  }
}
