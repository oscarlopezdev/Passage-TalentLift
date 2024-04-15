// Get the modal
var modal = document.getElementById("info-modal");
var currentLevel = document.getElementById('current-level');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the page loads, show the modal
window.onload = function() {
    var currentLevelInt = parseInt(currentLevel.textContent);
    if (currentLevelInt===1){
        modal.style.display = "block";
    }
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}