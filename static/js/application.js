$( document ).ready(function() {
	$( "#new_task" ).click(function() {
  		alert( "Handler for .click() called." );
	});

	$("#update_project_form").submit(function(e) {
		e.preventDefault();
    $.ajax({
       type: "POST",
       url: "http://localhost:8000/project/update/",
       data: $("#update_project_form").serialize(), 
       success: function(response)
       {
       		console.log(response.result)
       }
     });
	});
});