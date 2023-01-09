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
$(document).on('change','#formrecobros #tiporecobroInput',function(){
  var tip = document.getElementById('tiporecobroInput').value;
  if(tip === 'Tutelas'){
    $('.aa1').remove();
    $('.tiporecobrodiv').append(
      '<div class="row aa1">'+
          '<div class="col-md-3">'+
            '<label for="numfallo" class="form-label">numfallo</label>'+
            '<input type="text" class="form-control" id="numfallo" name="numfallo" required>'+
          '</div>'+
          '<div class="col-md-3">'+
            '<label for="fefallo" class="form-label">fefallo</label>'+
            '<input type="date" class="form-control" id="fefallo" name="fefallo" required>'+
          '</div>'+
          '<div class="col-md-3">'+
            '<label for="numAutoridadJudicial" class="form-label">NumAutoridadJudicial</label>'+
            '<input type="number" class="form-control" id="numAutoridadJudicial" name="numAutoridadJudicial" required>'+
          '</div>'+
          '<div class="col-md-3">'+
           '<label for="codcausal" class="form-label">codcausal</label>'+
            '<select class="form-control" id="codcausal" name="codcausal">'+
              '<option value="2">Servicios No POS</option>'+
              '<option value="3">Medicamentos</option>'+
              '<option value="5">Otras Causas</option>'+
              '<option value="7">Tratamiento integral</option>'+
            '</select>'+
          '</div>'+

          '<div class="col-md-3">'+
            '<label for="codigodane" class="form-label">Codigo_Dane</label>'+
            '<input type="number" class="form-control" id="codigodane" name="codigodane" required>'+
          '</div>'+
          '<div class="col-md-9">'+
            '<label for="tipoautoridadjudicial" class="form-label">Tipoautoridad_judicial</label>'+
            '<textarea rows="1" class="form-control border-width-2 col-md-12" value="" id="tipoautoridadjudicial" name="tipoautoridadjudicial" placeholder="Tipautoridadjudicial">'+
            '</textarea>'+
          '</div>'+
        '</div>'
        )
      }else {
        $('.aa1').remove();
      }
    })
