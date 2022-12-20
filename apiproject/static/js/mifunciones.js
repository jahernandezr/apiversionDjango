"use strict"
var getUrl = window.location;
var baseUrl = getUrl.protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];

$(document).on('change','#nitprestador',function(){
  var nitprestador=$('#nitprestador').val();
  alert(nitprestador);
  $.ajax({
      url: baseUrl+'/buscarnit/',
      type: 'POST',
      data: {'nitprestador': nitprestador,csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
      dataType: 'json',
      async: false,
      success:function(data){
        data.forEach(function(dat){
          //console.log(dat['fields'].nitprestador);
           $('#nombreprestador3').append('<label for="nombreprestador" class="form-label">nombreprestador</label>'+
           '<textarea value="'+ dat['fields'].nombreprestador +'" type="text" class="form-control" rows="1" id="nombreprestador" name="nombreprestador" required>'+ dat['fields'].nombreprestador +'</textarea>'
 //          $('#nombreprestador').html(dat['fields'].nombreprestador);
// <label for="nombreprestador" class="form-label">nombreprestador</label>
// <textarea value="" type="text" class="form-control" rows="1" id="nombreprestador" name="nombreprestador" required></textarea>
          );
        });
      }
  })
});
$(document).on('click','.navbar-toggler-icon',function(){
  var inputemail = document.getElementById('inputemail').value;
  $.ajax({
      url: baseUrl+'/buscarmodulos/',
      type: 'POST',
      data: {'inputemail': inputemail, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
      dataType: 'json',
      async: false,
      success:function(data){
        $('#aurlinicios').remove();
        data.forEach(function(i){
           $('#divurlinicio').append('<a id="aurlinicios" class="nav-link active" aria-current="page" href="'+baseUrl+'/'+i['fields'].urlaplicativo+'/'+'" style="color:grey">'+i['fields'].nombremodulo+'</a>')
        });
     }
   })
})
