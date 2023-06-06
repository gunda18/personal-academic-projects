function validate()                
{ 
  var username = document.forms["loginform"]["username"];      
  var password = document.forms["loginform"]["password"]; 
  if (username.value == "" || password.value == "" )                
  { 
    window.alert("Username and Password cannot be empty"); 
    return false; 
  } 
  return true; 
}