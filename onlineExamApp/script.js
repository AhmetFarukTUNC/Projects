//pulling json data

var connection = new XMLHttpRequest();
let returningFromServer;
connection.onreadystatechange=function () { 
    if (this.readyState == 4 && this.status == 200) {
        returningFromServer = JSON.parse(connection.responseText);
       
        bringQuestion();
    }
    return returningFromServer;
 };

 connection.open("GET","data.json",true);
 
 connection.send();

 // We describe variables...

const resultArea = document.getElementsByClassName("showQuestion")[0];

const question = document.getElementById("question");

const options = document.getElementsByName("option");

const descriptionA = document.getElementById("descriptionA");

const descriptionB = document.getElementById("descriptionB");
const descriptionC = document.getElementById("descriptionC");

const descriptionD = document.getElementById("descriptionD");

const  sendExamButton = document.getElementById("sendExam");
let point = 0;
let order = 0;
function bringQuestion() { 
   clearSelection();
   console.log(returningFromServer)

   let nextQuestion = returningFromServer.questions[order];
   question.innerHTML = nextQuestion.question;
   descriptionA.innerText = nextQuestion.optionA;
   descriptionB.innerText = nextQuestion.optionB;
   descriptionC.innerText = nextQuestion.optionC;
   descriptionD.innerText = nextQuestion.optionD;
}
function clearSelection() { 
    options.forEach(option => option.checked = false);
}

function getSelection() { 
    let vote;
    options.forEach(option => {
        if (option.checked == true) {
            vote = option.id;
        }
        
        
    })
    return vote;
 }

sendExamButton.addEventListener("click",() => {
    const chosen =getSelection();
    console.log(chosen)
    console.log(returningFromServer.questions[order].trueResult)
    if (chosen) {
        if (chosen === returningFromServer.questions[order].trueResult) {
            point++;
        }

    }
    order++;

    if (order < returningFromServer.questions.length) {
        bringQuestion();
    }

    else{
       resultArea.innerHTML = `
       <h2>Mevcut Sorular içerisinden ${point}/${returningFromServer.questions.length} oranında başarı sağladı.</h2>
       `

       sendExamButton.setAttribute("onclick","location.reload()")
       sendExamButton.innerHTML = ("Yeniden Başla")
    }

});