// Funcion para validar campos form
const checkInputsForm = () => {
    const nombre = $("#nombre").val();
    const descripcion = $("#descripcion").val();
    if (nombre === "" || descripcion === "") {
        $("#btn-submit").attr("disabled", true);
    } else {
        $("#btn-submit").attr("disabled", false);
    }
};

// Eventos para validar campos form
$("#modalBody").on({
    keyup: checkInputsForm,
    change: checkInputsForm,
});


// CREAR DOCUMENTO
const btnCreateDocument = async() => {
    const formCreate = await fetch("creardocumento/", {
            method: "GET",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            credentials: "same-origin",
        })
        .then((response) => response.text())
        .then((data) => data);
    customizeForm(formCreate, "creardocumento/", "Crear Documento", "Crear");
};

// ACTUALIZAR DOCUMENTO
const btnUpdate = async(id) => {
    $("#modalBody").empty();
    const formUpdate = await fetch(`actualizardocumento/${id}/`, {
            method: "GET",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            credentials: "same-origin",
        })
        .then((response) => response.text())
        .then((data) => data);
    customizeForm(formUpdate, `actualizardocumento/${id}/`, "Actualizar Documento", "Actualizar");
};

// BORRAR DOCUMENTO
const btnDelete = (id) => {
    fetch(`eliminardocumento/${id}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
        },
        credentials: "same-origin",
    }).then((response) => {
        if (response.ok) {
            alert("Documento eliminado");
            window.location.reload();
        } else {
            throw new Error("Error al eliminar");
        }
    });
};