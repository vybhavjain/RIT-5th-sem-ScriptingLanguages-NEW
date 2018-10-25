<html>
<body>
Subject 1 <input type="text" id="sub1_marks" onkeyup="validate(1)"/>  <div id="sub1_alerts"></div><br>
Subject 2 <input type="text" id="sub2_marks" onkeyup="validate(2)"/> <div id="sub2_alerts"></div>
<button id="get_grade" onclick="get_results();">Get Grade</button>
<script>

function validate(id)
{
	var m_id="sub"+id+"_marks";
	var a_id="sub"+id+"_alerts";
	var marks=document.getElementById(m_id).value;
	document.getElementById(a_id).innerHTML="";
	if(isNaN(marks))
		document.getElementById(a_id).innerHTML="Only numbers are supported";
	else
	{
		if(marks>100 || marks<0)
			document.getElementById(a_id).innerHTML="Marks must be between 1 and 100";
	
	}
}
function get_results()
{
	var sub1_marks=document.getElementById("sub1_marks").value;
	var sub2_marks=document.getElementById("sub2_marks").value;
	document.getElementById("sub1_alerts").innerHTML=get_grade(sub1_marks)+" "+"Grade";
	document.getElementById("sub2_alerts").innerHTML=get_grade(sub2_marks)+" "+"Grade";
}

function get_grade(marks)
{
	if(marks>90)
		return "S+"
	else if(marks>80)
		return "S"
	else if(marks>70)
		return "A"
	else if(marks>60)
		return "B"
	else if(marks>50)
		return "C"
	else if(marks>40)
		return "D"
	else 
		return "Fail"
}
</script>
</body>
</html>
