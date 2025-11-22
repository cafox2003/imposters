const front = document.getElementById("front-side");
const back = document.getElementById("back-side");
const flipBtn = document.getElementById("flip-btn");

let showFront = true;
console.log("Show front: ", showFront);

flipBtn.addEventListener("click", ()=> {
  if (showFront) {
    front.classList.add("hidden");
    back.classList.remove("hidden");
  } else {
    back.classList.add("hidden");
    front.classList.remove("hidden");
  }
  showFront = !showFront;
});

