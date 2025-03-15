document.addEventListener("DOMContentLoaded", function () {
    console.log("GranaMap carregado!");

    let deleteButtons = document.querySelectorAll(".delete-btn");
    deleteButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            if (!confirm("Tem certeza que deseja remover este valor?")) {
                event.preventDefault();
            }
        });
    });
});
