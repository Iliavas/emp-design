document.getElementById("menu-button").onclick = () => {
  console.log(window.innerHeight, window.innerWidth)
  let x = (window.innerWidth + window.innerHeight) * 0.65;
  let menu = document.getElementById("menu");
  menu.style.transform = `translate(-${x}px, -${x}px)`;
  document.getElementById("grad").style.display = "none";
  setTimeout((e) => {
    let menu_content = document.getElementById("menu-content")
    menu_content.style.display = "flex";

    menu_content.style.opacity = 1;
  },500)
  //menu.style.top = 0;
}
document.getElementById("cross").onclick = () => {
  let menu_content = document.getElementById("menu-content")
  menu_content.style.display = "none";
  let menu = document.getElementById("menu");
  menu.style.transform = "translate(calc(1.41421 * (100vw + 100vh)), calc(1.41421 * (100vw + 100vh)))";

  document.getElementById("grad").style.display = "block";
}