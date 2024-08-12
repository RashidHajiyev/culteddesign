const textarea = document.getElementById("message");
const charCounter = document.getElementById("charCounter");

textarea.addEventListener("input", () => {
  const currentLength = textarea.value.length;
  charCounter.textContent = `${currentLength}/300`;
});