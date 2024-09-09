// Load quizzes from a JSON file
let quizzes;
fetch('quizzes.json')
  .then(response => response.json())
  .then(data => {
    quizzes = data;
    loadQuizTopics();
});

const quizContainer = document.getElementById('quizContainer');
const quizTopicsElement = document.getElementById('quizTopics');
let currentTopic = '';
let currentQuiz = [];
let questionIndex = 0;
let correctAnswers = 0;
let progress = 0;
const limitQuestions = 10;
let maxQuestions = limitQuestions;


// Load topics into the index page
function loadQuizTopics() {
  for (let topic in quizzes) {
    const li = document.createElement('li');
    li.innerHTML = topic;
    li.onclick = () => startQuiz(topic);
    quizTopicsElement.appendChild(li);
  }
}

// Display a quiz question
function showQuestion() {
  const question = currentQuiz[questionIndex];
  // Shuffle answers with their indices
  const shuffledAnswers = question.answers
    .map((answer, index) => ({ answer, index }))  // Create array of objects with answers and their indices
    .sort(() => Math.random() - 0.5);             // Shuffle the array
  
  quizContainer.style.display = 'block';
  quizContainer.innerHTML = `
    <button onclick="goBackToTopics()">Zurück zur Übersicht</button>
    <div class="progress-bar">
        <div class="progress-bar-fill"></div>
    </div>
    <h1>${currentTopic}</h1>
    <h2>${question.quizTitle}</h2>
    <p>${question.task}</p>
    <div class="answers">
      ${shuffledAnswers.map((item) => `<button onclick="checkAnswer(${item.index})" index=${item.index}>${item.answer}</button>`).join('')}
    </div>
    <button id="nextButton" onclick="nextQuestion()" disabled>Next</button>
  `;
}

// Check if the selected answer is correct
function checkAnswer(selectedIndex) {
  const buttons = document.querySelectorAll('.answers button');
  buttons.forEach((btn) => {
    let index = parseInt(btn.getAttribute("index"))
    btn.disabled = true;
    if (index === selectedIndex) {
      btn.style.backgroundColor = index === 0 ? 'green' : 'red';
      correctAnswers++
    }
    if (index === 0 && index !== selectedIndex) {
      btn.style.backgroundColor = 'green';
      correctAnswers--
    }
  });
  document.getElementById('nextButton').disabled = false;
  updateProgress();
}

// Load the next question
function nextQuestion() {
  questionIndex++;
  if (questionIndex < currentQuiz.length) {
    showQuestion();
  } else {
    quizContainer.innerHTML = `
        <button onclick="goBackToTopics()">Back to Topics</button>
        <div class="progress-bar">
            <div class="progress-bar-fill"></div>
        </div>
        <h1>${currentTopic}</h1>
        <h2>Quiz abgeschlossen!</h2>
        <p>Du hast ${correctAnswers} von ${maxQuestions} Fragen richtig beantwortet.</p>
    `;
  }
document.querySelector('.progress-bar-fill').style.width = progress + '%';
}

// Start a quiz from a specific topic
function startQuiz(topic) {
    // Hide topic selection and show quiz container
    document.getElementById('topicSelection').style.display = 'none';
    document.getElementById('quizContainer').style.display = 'block';
  
    currentTopic = topic;
    currentQuiz = shuffleArray(quizzes[topic]);
    maxQuestions = Math.min(currentQuiz.length,limitQuestions);
    currentQuiz = currentQuiz.slice(0, maxQuestions);
    correctAnswers = 0;
    questionIndex = 0;
    progress = 0;
    showQuestion();
    document.querySelector('.progress-bar-fill').style.width = '0%';
}
  
  // Go back to the topic selection
  function goBackToTopics() {
    document.getElementById('quizContainer').style.display = 'none';
    document.getElementById('topicSelection').style.display = 'block';
    quizTopicsElement.innerHTML = '';
    loadQuizTopics();
}
  

// Shuffle array function for random question selection
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

// Update the progress bar
function updateProgress() {
  progress = ((questionIndex + 1) / maxQuestions) * 100;
  document.querySelector('.progress-bar-fill').style.width = progress + '%';
}
