function validate()                
{ 
  var fullname = document.forms["signupform"]["fullname"];
  var username = document.forms["signupform"]["username"];
  var email = document.forms["signupform"]["email"]; 
  var number = document.forms["signupform"]["number"];     
  var password1 = document.forms["signupform"]["password1"];
  var password2 = document.forms["signupform"]["password2"]; 
  var month = document.forms["signupform"]["dobmonth"];
  var date = document.forms["signupform"]["dobday"];
  var year = document.forms["signupform"]["dobyear"];
  var gender = document.forms["signupform"]["gender"]
  var letters = /^[A-Za-z]+$/;
  var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  var phoneno = /^\d{10}$/;
  var month = document.forms["signupform"]["dobmonth"];
  var userletter = /^[A-Za-z0-9]+$/;


//name
  if (fullname.value == "")                
  { 
    window.alert("Name cannot be empty."); 
    username.focus(); 
    return false; 
  }
  if (fullname.value.match(letters))
  {
  }
  else
  {
  	window.alert("Name should contain only alphabets.");
  	return false;
  }

  //username
  if (username.value == "")
  {
    window.alert("Username cannot br empty.");
    return false;
  }
  if (username.value.match(userletter))
  {
  }
  else
  {
    window.alert("Username should contain only Letters and Numbers.");
    return false;
  }

//email
  if (email.value == "")
  {
  	window.alert("Email cannot be empty.");
  	return false; 
  }  
  if (email.value.match(filter)) 
  {
  }
  else
  {
  	window.alert("Invalid Email Adress.");
  	return false;
  }

//mobile number  
  if (number.value == "")
  {
  	window.alert("Mobile Number cannot be empty.");
  	return false; 
  } 
  if (number.value.match(phoneno))
  {
  }
  else
  {
  	window.alert("Mobile number should contain only 10 digits.");
  	return false;
  }

  //password  
  if (password1.value =="")
  {
  	window.alert("Password cannot be empty.");
  	return false;
  }
  if (password1.value == password2.value)
  {
  	if(password1.value.length < 8)
  	{
  		window.alert("Password must be atleast 8 characters length.");
  		return false;
  	}
  	if (password1.value == fullname.value) 
  	{
  		window.alert("Password must be different from your Name.");
  		return false;
  	}
  	re = /[0-9]/;
  	if (!re.test(password1.value)) 
  	{
  		window.alert("Password must contain at least one digit (0-9).");
  		return false;
  	}
  	re = /[A-Z]/;
  	if (!re.test(password2.value)) 
  	{
  		window.alert("Password muat contain at least one UpperCase Letter (A-Z).");
  		return false;
  	}
  	re = /[a-z]/;
  	if (!re.test(password2.value)) 
  	{
  		window.alert("Password muat contain at least one LowerCase Letter (a-z).");
  		return false;
  	}
  }
  else
  {
  	window.alert("Passwords doesn't match.");
  	return false;
  }

  //date
  if(month.value == "Month")
  {
    window.alert("Please enter correct Date of Birth");
    return false;
  }
  if(year.value == "0000")
  {
    window.alert("Please enter correct Date of Birth");
    return false;
  }
  if(date.value == "0")
  {
    window.alert("Please enter correct Date of Birth");
    return false;
  }
  if(month.value == "february")
  {
    if (date.value > 28)
    {
      window.alert("Invalid Date of Birth");
      return false;
    }
  }
  return true; 
}