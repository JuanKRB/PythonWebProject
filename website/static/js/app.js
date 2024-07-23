const btn_iniciar = document.querySelector("#btn-iniciar");
const btn_registrarse = document.querySelector("#btn-registrarse");
const contenedor = document.querySelector(".contenedor");

btn_registrarse.addEventListener("click", () => {
  contenedor.classList.add("modo-registrarse");
});

btn_iniciar.addEventListener("click", () => {
  contenedor.classList.remove("modo-registrarse");
});
