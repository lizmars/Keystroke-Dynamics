var url_k = 'http://162.243.145.18:80/auth'
var keylog = [];
var timelog = [];
var username;

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

function auth_next(){
  if(document.getElementById("userIDauth").value.length != 0){
    if(document.getElementById("name_status_Auth").style.color == "green"){
      document.getElementById("AuthStep2").style.display = "block"
      document.getElementById("placehld").innerHTML = document.getElementById("userIDauth").value
      document.getElementById("nextstep").disabled = true
      $("html, body").animate({ scrollTop: $(document).height() }, 1000);
      document.getElementById("keyrec").focus();
    }
    else{
      alert("Please Chose Valid Name");
    }
  }
  else{
    alert("Enter username first");
  }

}

function checknameA(){
 var name=document.getElementById( "userIDauth" ).value;
 if (document.getElementById( "userIDauth" ).value.length == 0){
   document.getElementById("nextstep").disabled = true;
 }

 if(name){
   $.ajax({
       url: url_k,
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

function auth(){
  username = $("#placehld").text();

  keylog.toString();
  s = timelog[0]/1000.0;
  for(i = 0; i < timelog.length; i++ ){
    timelog[i] = (timelog[i]/1000.0) - s;
  }
  timelog.toString();

  param = '{ "' + username + '" : [' +
  '{ "Keys":"'+ keylog + '" , "Times":"' + timelog +'" }]}';
  $.ajax({
      url: url_k,
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
