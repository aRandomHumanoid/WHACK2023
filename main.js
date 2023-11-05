function scrollToButtons() {
  // Scrolls to the "Host Event" or "Browse" buttons
  window.scrollTo(401, 800);
}

function goToPostForm() {
  // Scrolls to the post form after "Host Event" button is clicked
  document.getElementById("post-form-container").style.display = "flex";
  window.scrollTo(401, 1610);
}

function squishCal() {
  //NONFUNCTIONAL
  document.getElementById("calendar-container").style.width = "50%";
}
