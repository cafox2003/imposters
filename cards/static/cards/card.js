const front = document.getElementById("front-side");
const back = document.getElementById("back-side");
const cardContainer = document.querySelector(".card-container");

let showFront = true;

function flipCard() {
  front.classList.toggle("hidden");
  back.classList.toggle("hidden");
}

function showPreviousCard() {
  document.getElementById("prev-link").click();
}

function showNextCard() {
  document.getElementById("next-link").click();
}

cardContainer.addEventListener("click", flipCard);

document.addEventListener("keydown", (e) => {
  switch (e.key) {
    case "ArrowLeft":
      showPreviousCard();
      break;

    case "ArrowRight":
      showNextCard();
      break;

    case " ":
    case "ArrowUp":
    case "Enter":
      e.preventDefault();   // avoid scrolling
      flipCard();
      break;
  }
});
