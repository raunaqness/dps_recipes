


var formdata = {};

function addIngredient(){
    console.log("gg");
    var baseDiv = document.getElementsByClassName('ingredients');
    var n = document.getElementsByClassName('ingredients')[0].children.length;
    console.log(n);
    var nextIndex = n + 1;
    console.log(nextIndex);

    var newHTML = `
    <div class="form-group row" style="margin:0px 0px 10px 0px;">
        <div class="col-xs-6" >
        <label for="ingredient-${nextIndex}">Name</label>
        <input type="text" class="form-control" id="ingredient-${nextIndex}" 
        name="ingredient-${nextIndex}" oninput="input_updated(this)"/>
        </div>
        <div class="col-xs-6">
        <label for="quantity-${nextIndex}">Quantity</label>
        <input type="number" class="form-control" id="quantity-${nextIndex}" 
        name="quantity-${nextIndex}" oninput="input_updated(this)" />
        </div>  
    </div>
    `

    $(baseDiv).append(newHTML);
}

function input_updated(data){
      formdata[data.name] = data.value;
  }


function getFormData(dom_query){
    var out = {};
    var s_data = $(dom_query).serializeArray();
    //transform into simple data/value object
    for(var i = 0; i<s_data.length; i++){
        var record = s_data[i];
        out[record.name] = record.value;
    }
    return out;
}

function formSubmit(){
    // var formData = new FormData(formdata);
    var form_data = new FormData();

    for ( var k in formdata) {
        form_data.append(k, formdata[k]);
    }

    var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    form_data.append('image', $('input[type=file]')[0].files[0]);

    $.ajax({
        url: '',
        type: 'POST',
        data: form_data,
        headers: {
          'X-CSRFToken' : csrf_token,
        },
        processData: false,
        contentType: false,
        async: true,
        cache: false,
        enctype: "multipart/form-data",
        dataType: "json",
        success: function(msg) {
            if (msg.success){
              window.location.href = msg.redirect;
            }
        }
    });
}

$("button").click(function(e){
    
    e.preventDefault();
    if (this.id == "addIngredient"){
        
        addIngredient();
    }

    if (this.id == "submit"){
        console.log("submit");
        formSubmit();
    }

    
  });


