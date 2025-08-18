const senhaInput = document.getElementById("senha");
const eyeOpen = document.getElementById("toggle-senha");
const eyeClosed = document.getElementById("toggle-senha-hidden");

eyeClosed.addEventListener("click", () => {
  senhaInput.type = "text"; // Mostrar a senha
  eyeClosed.classList.add("hidden");
  eyeOpen.classList.remove("hidden");
});

eyeOpen.addEventListener("click", () => {
  senhaInput.type = "password"; // Esconder a senha
  eyeOpen.classList.add("hidden");
  eyeClosed.classList.remove("hidden");
});