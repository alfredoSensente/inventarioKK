let path="/empleado/generador/"

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function PasarValor(valor1, valor2, codigo, URL){
        let letra1 = document.getElementById(valor1).value.charAt(0);
        let letra2 = document.getElementById(valor2).value.charAt(0);
        console.log(letra1);
        console.log(letra2);
        ObtenerCodigo(letra1, letra2, codigo, path)
}

function SelectPasarValor(valor1, valor2, codigo, URL) {

    var combo1 = document.getElementById(valor1);
    var selected1 = combo1.options[combo1.selectedIndex].text.charAt(0);
    var combo2 = document.getElementById(valor2);
    var selected2 = combo2.options[combo2.selectedIndex].text.charAt(0);

    if (combo1.value!=0 && combo2.value!=0) {

        ObtenerCodigo(selected1, selected2, codigo, URL)   

    }
    
}

function ObtenerCodigo(letra1, letra2, codigo, URL) {
    const csrftoken = getCookie('csrftoken');
    console.log('llego a obtener codigo')
    if (letra1!="" &&  letra2!="") {
        let letras = letra1 + '' + letra2;
        let data ={
                    'csrfmiddlewaretoken':csrftoken,
                    'letras':letras,
                    };
        console.log(URL)
        $.post(URL, data, function(response){ 
                document.getElementById(codigo).value = response
        });
    }
}