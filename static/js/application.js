$( document ).ready(function() {
	$( "#new_task_" ).click(function() {
  		$("#pop").show()
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

function deselect(e) {
  $('.pop').slideFadeToggle(function() {
    e.removeClass('selected');
  });    
}

$(function() {
  $('#contact').on('click', function() {
    if($(this).hasClass('selected')) {
      deselect($(this));               
    } else {
      $(this).addClass('selected');
      $('.pop').slideFadeToggle();
    }
    return false;
  });

  $('.close').on('click', function() {
    deselect($('#contact'));
    return false;
  });
});

$.fn.slideFadeToggle = function(easing, callback) {
  return this.animate({ opacity: 'toggle', height: 'toggle' }, 'fast', easing, callback);
};


});