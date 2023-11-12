const messageWindow = document.querySelector(".message-window");
const scrollToLatest = document.querySelector("#scroll-to-latest");

if (messageWindow.offsetHeight < messageWindow.scrollHeight) {
  scrollToLatest.style.display = "block";
}

scrollToLatest.addEventListener("click", () => {
  Array.from(document.querySelectorAll(".message"))
    .pop()
    .scrollIntoView({ behavior: "smooth", block: "end" });
});

messageWindow.addEventListener("scroll", () => {
  const scrollBottom = messageWindow.scrollTop + messageWindow.offsetHeight;
  if (messageWindow.scrollHeight <= scrollBottom + window.innerHeight / 1.5) {
    if (!scrollToLatest.classList.contains("hidden")) {
      scrollToLatest.classList.add("hidden");
    }
  } else {
    scrollToLatest.classList.remove("hidden");
  }
});
