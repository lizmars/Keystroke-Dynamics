var url_k = 'http://localhost:5000/createprofile'
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

function checkname(){
 var name=document.getElementById( "userID" ).value;
 if (document.getElementById( "userID" ).value.length == 0){
   document.getElementById("nexstep").disabled = true;
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
       success: function(response) {
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
      },
      error: function(error) {
          console.log(error);
      }
     });
 }
 else{
  $( '#name_status' ).html("");
  return false;
 }

}

function cp_next(){
  if(document.getElementById("userID").value.length != 0){
    if(document.getElementById("name_status").style.color == "green"){
      document.getElementById("CPStep2").style.display = "block";
      document.getElementById("keysrec").focus();
      $("html, body").animate({ scrollTop: $(document).height() }, 1000);
      document.getElementById("placehold").innerHTML = document.getElementById("userID").value;
      document.getElementById("nexstep").disabled = true;
    }
    else{
      alert("Please Enter Different Name");
    }

  }
  else{
    alert("Enter username first");
  }
}


function submit() {
  username = $("#placehold").text();

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
            url: url_k,
            headers: {
                'Type':'Create_Profile',
                'User':username,
                'Content-Type':'application/json'
            },
            method: 'POST',
            data: parameters,
            success: function(result){
              document.getElementById("sub").disabled = true;
              //document.getElementById("keysrec").value = "";
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

    //document.getElementById("keysrec").value = "";
    //document.getElementById("Bar").style.width = 1 + "px";
    document.getElementById("placehold").value = "";
  }
  else {
    alert("Enter some text first") //if texarea is empty
  }
}
