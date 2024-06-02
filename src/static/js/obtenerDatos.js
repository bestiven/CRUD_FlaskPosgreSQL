console.log('funcionando')
function obtenerDatos(id){
    document.getElementById('formulario').action= '/editar_persona/' +id
    document.getElementById('boton').innerHTML ='Actualizar'

    nombreactual =document.getElementById('tabla_nombre'+id).innerHTML
    apellidoactual =document.getElementById('tabla_apellido'+id).innerHTML
    telefonoactual =document.getElementById('tabla_telefono'+id).innerHTML

    document.getElementById('nombre').value = nombreactual
    document.getElementById('apellido').value = apellidoactual
    document.getElementById('telefono').value = telefonoactual
}
