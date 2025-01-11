// Function to clear the result when user starts typing again
function clearResult() {
    const resultContainer = document.getElementById("resultContainer");
    const resultText = document.getElementById("resultText");

    if (resultText) {
        resultText.innerHTML = "";  // Clear the result text
    }

    if (resultContainer) {
        resultContainer.style.display = "none";  // Hide the result container
    }
}
