// Obtener el elemento del botón y el contador
var clearButton = document.getElementById('clear-button');
var currentLevel = document.getElementById('current-level');
var warningMessage = document.getElementById('warning-message');
var startTime = null;
const textAnswer = document.getElementById('text-answer');
const textChallenge = document.getElementById('text-challenge');
const wordsPerMinute = document.getElementById('words-per-minute');
// Verificar si ya hay un valor almacenado en localStorage
if(localStorage.getItem('level')) {
    currentLevel.textContent = localStorage.getItem('level');
}

const challenges = [
    "mr. dursley was",
    "the director of a firm called grunnings, which made",
    "drills. he was a big, beefy man with hardly any neck.",
    "which came in very useful as she spent so much of her time",
    "the dursleys had a small son called dudley and in their opinion.",
    "weeds were not the only things frank had to contend with either...",
    "beds in fine weather, even though the weeds were starting to creep up.",
    "was that somebody would discover it. they did not think they could bear.",
    "potter was mrs. dursley sister, but they had not met for several years in fact.",
    "the dursleys had everything they wanted, but they also had a secret, and their greatest"
];


// Añadir un evento de clic al botón de limpieza
clearButton.addEventListener('click', function() {
    // Clear data to level 1
    first_level = 1
    localStorage.setItem('level', first_level);
    currentLevel.textContent = first_level;
    load_next_challenge_text()
    warningMessage.textContent = ""
    textAnswer.textContent = ""
});

document.addEventListener("DOMContentLoaded", function() {
    startTime = Date.now();
    load_next_challenge_text()
});

function load_next_challenge_text(){
    var currentLevelInt = parseInt(currentLevel.textContent);
    // Texto del array en la posición 0
    const text = challenges[currentLevelInt-1];

    // Establecer el contenido del div igual al texto
    textChallenge.textContent = text;
    currentLevel.textContent = localStorage.getItem('level') !== null ? localStorage.getItem('level') : 1;
}


// Agregar evento keydown al documento
document.addEventListener('keydown', function(event) {
    // Obtener el carácter tecleado por el usuario
    const keyPressed = event.key;
    let text_answer = textAnswer.textContent + keyPressed;
    let text_challeng = textChallenge.textContent;


    if (validateInput(text_answer, text_challeng)){
        textAnswer.textContent = text_answer;

        if (text_answer === text_challeng){
            try_level_up(text_answer)
        }
    }

});

function try_level_up(text_answer){
    const typingSpeed = calculateWordPerMinute(text_answer);
    if (isSuccessLesson(typingSpeed)){
        level_up()
    }else{
        show_to_slow_message()
    }
    update_word_per_minute(typingSpeed)
}
function isSuccessLesson(typingSpeed){
    const REQUIRED_WORDS_PER_MINUTE = 27
    return typingSpeed > REQUIRED_WORDS_PER_MINUTE
}
function calculateWordPerMinute(text_answer){

     // Record the end time
     endTime = new Date();
    
     // Get the text input
     const textInput = text_answer.trim();
     
     // Split the input text into words
     const words = textInput.split(/\s+/);
     
     // Calculate the number of words
     const wordCount = words.length;
     
     // Calculate the time spent typing (in milliseconds)
     const timeSpent = endTime - startTime;
     
     // Convert time to minutes
     const timeInMinutes = timeSpent / (60 * 1000);
     
     // Calculate words per minute (WPM)
     const wpm = Math.round(wordCount / timeInMinutes);

     return wpm
}
function update_word_per_minute(typingSpeed){
    wordsPerMinute.textContent = typingSpeed
}
function show_to_slow_message(){
    textAnswer.textContent = "";
    warningMessage.textContent = "Could you type a bit faster. Please try again!";
}
function level_up(){
    upgrade_level()
    load_next_challenge()
}

function load_next_challenge(){
    textAnswer.textContent = "";
    load_next_challenge_text()
}
function upgrade_level(){
    // Obtener el valor actual del contador
    var currentLevelInt = parseInt(currentLevel.textContent);
    // Incrementar el contador
    currentLevelInt++;
    // Actualizar el valor del contador en el span y en el almacenamiento local
    currentLevel.textContent = currentLevelInt;
    localStorage.setItem('level', currentLevelInt);
}

function validateInput(input, challenge) {
    // Get the index to be validated
    const index = input.length - 1;

    if (index === 0){
        startNewAnswer()
    }
    // Compare same index in both texts
    return input[index] === challenge[index];
}

function startNewAnswer(){
    startTime = Date.now();
    warningMessage.textContent = ""
}