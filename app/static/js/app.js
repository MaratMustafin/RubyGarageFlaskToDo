$(document).ready(function() {
        $('table tbody').sortable({
         update: function(event, ui) {
                   $(this).children().each(function (index) {
                        if ($(this).attr('data-position') != (index+1)) {
                            $(this).attr('data-position', (index+1)).addClass('updated');
                        }
                        });
                      saveNewPositions();
                   }
        });
      });
function saveNewPositions() {
            var positions = [];
            $('.updated').each(function () {
               positions.push([$(this).attr('data-index'), $(this).attr('data-position')]);
               $(this).removeClass('updated');
            });

            $.ajax({
               url: '/change_pos',
               method: 'POST',
               dataType: 'text',
               data: {
                   update: 1,
                   positions: JSON.stringify(positions)
               }, success: function (response) {
                    console.log(response);
               }
            });
        }
                $(document).on("click", ".trash_task", function() { 
                  console.log($(this).attr("data-id"));
                var el = this
                $.ajax({
                  url: "/delete_task",
                  type: "POST",
                  cache: false,
                  data:{
                    id: $(this).attr("data-id")
                  },
                  success: function(response){
                       if(response == 'success'){
                         // Remove row from HTML Table
                         $(el).closest('tr').css('background','tomato');
                         $(el).closest('tr').fadeOut(800,function(){
                            $(this).remove();
                         });
                            }else{
                         alert('Invalid ID.');
                            }
                  }
                });
              });
$(document).on("click", ".trash", function() { 
                var el = this
                $.ajax({
                  url: "/delete_project",
                  type: "POST",
                  cache: false,
                  data:{
                    id: $(this).attr("id")
                  },
                  success: function(response){
                       if(response == 'success'){
                         // Remove row from HTML Table
                         $(el).closest('div').css('background','tomato');
                         $(el).closest('div').fadeOut(800,function(){
                            $(this).remove();
                         });
                            }else{
                         alert('Invalid ID.');
                            }
                  }
                });
              });

$(document).ready(function() {
$("td#main_task").mouseover(function(){
     $("button#del_button").fadeIn();
     $("button#upd_button").fadeIn();
 });

$("td#main_task").mouseleave(function(){
     $("button#del_button").fadeOut();
     $("button#upd_button").fadeOut();
  })
 ;});

/*            $(function () {

              $('#updateForm').on('submit', function (e) {
                e.preventDefault();
                console.log($('input#project_name').val());

                $.ajax({
                  type: 'POST',
                  url: '/update_project',
                  data: $('#updateForm').serialize(),
                  success: function(data) {
                    $('span#project_name').fadeOut(800,function(){
                      $(this).remove;
                    });
                    $('span#project_name').fadeOut(800,function(){
                      $(this).add(data.project_name);
                    });                    
                  }
                });

              });

            });*/
/*$(document).on("click",".add",function() {
  var task_name = $('input#task_name').val();
  var task_date = $('input#task_date').val();
  var task_priority = $('input#rangeInput').val();
  var project_id = $(this).attr('data-id');
    $.ajax({
      url: "/add_task",
      type: "POST",
      dataType: 'text',
      data: {
        task_name: task_name,
        task_date: task_date,
        task_priority: task_priority,
        project_id: project_id
      },
      success: function(response) {
        console.log(response);
      }
    });
});*/