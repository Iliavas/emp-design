document.getElementById("menu-button").onclick = () => {
  let menu = document.getElementById("menu");
  menu.style.transform = "translate(-100vw, -100vh)";
  document.getElementById("grad").style.display = "none";
  //menu.style.top = 0;
}
document.getElementById("cross").onclick = () => {
  let menu = document.getElementById("menu");
  menu.style.transform = "translate(100vw, 100vh)";
  document.getElementById("grad").style.display = "block";
}