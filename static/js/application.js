$( document ).ready(function() {
	$( "#new_task" ).click(function() {
  		$("#dialog").dialog('open');
	});

	$("#update_project_form").submit(function(e) {
		e.preventDefault();
    $.ajax({
       type: "POST",
       url: "http://localhost:8000/project/update/",
       data: $("#update_project_form").serialize(), 
       success: function(response)
       {
        
       }
     });
	});

  $("#create_task").submit(function(e) {
    e.preventDefault();
    console.log("Se fue")
    $.ajax({
       type: "POST",
       url: "http://localhost:8000/project/task/create_task/",
       data: $("#create_task").serialize(), 
       success: function(response)
       {
          if(response.status == "200"){
            alert("Se creo una nueva tarea")
            task = "<a href='#'" + "class='collection-item'>" + response.title + "</a>"
            $( "#tasks" ).append( task )
          }
          console.log(response.status)
       }
     });
  });




});