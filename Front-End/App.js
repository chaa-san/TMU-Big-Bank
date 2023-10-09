import React, {useState} from 'react' // , useEffect 
import './App.css';


function App() {


  const [submitResult] = useState(''); // ,  setSubmitResult
  let inputValue = 0, state = 0;
  let loggedin = false;
  //states: 0 - not logged in, 1-5 are options, 6 is idle 
  const displayButtonNumber = (number) => {
    const displayBox = document.getElementById("display-box");
    if (displayBox.innerHTML.length < 4) {
    displayBox.innerHTML += number;
  }
  }
  const clearDisplay = () => {
    const displayBox = document.getElementById("display-box");
    displayBox.innerHTML = "";
  }
  const submit = () => {
    const displayBox = document.getElementById('display-box');
    inputValue = displayBox.innerHTML;
    const lols = document.getElementById('myInput').value;
    if (inputValue === '' || lols === ''){
      const displayBox2 = document.getElementById('display-box-2');
      displayBox2.innerHTML = "Empty Box!"
      return;
    }
    fetch('/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ input1: inputValue, input2: lols , input3: state})
    })
    .then(response => response.json())
    .then(data => {
      const displayBox2 = document.getElementById('display-box-2'); // Get the display-box-2 element
      displayBox.innerHTML = "";
      if (data.result === "Invalid Credentials!") {
        inputValue = 0
        displayBox2.innerHTML = data.result;
        displayBox2.style.color = 'red'; // Set the color to red for an error message
      } else {
        displayBox2.innerHTML = data.result;
        loggedin = true;
        state = 6;
        displayBox2.style.color = 'black'; // Set the color to black for a regular message
      }
    })
    .catch(error => {
      console.error(error);
    });
  };
  const deposit = (nam) => {
    const buttons = document.querySelectorAll('.button3');
    const button = document.getElementById(nam);
    buttons.forEach(button => {
      button.style.backgroundColor = '#004c9b';
    }); 
    button.style.backgroundColor = 'red';
    const displayBox2 = document.getElementById('display-box-2');

    if (!loggedin) {
      displayBox2.innerHTML = "Must Login first!";
    }else{
      displayBox2.innerHTML = "Enter a deposit amount!";
      state = 1;
    }

  }

  const withdraw = (nam) => {
    const buttons = document.querySelectorAll('.button3');
    const button = document.getElementById(nam);
    buttons.forEach(button => {
      button.style.backgroundColor = '#004c9b';
    }); 
    button.style.backgroundColor = 'red';
    const displayBox2 = document.getElementById('display-box-2');

    if (!loggedin) {
      displayBox2.innerHTML = "Must Login first!";
    }else{
      displayBox2.innerHTML = "Enter a Withdrawal amount!";
      state = 2;
    }
    
  }
  const transfer = (nam) => {
    const buttons = document.querySelectorAll('.button3');
    const button = document.getElementById(nam);
    buttons.forEach(button => {
      button.style.backgroundColor = '#004c9b';
    }); 
    button.style.backgroundColor = 'red';
    const displayBox2 = document.getElementById("display-box-2");
    if (!loggedin) {
      displayBox2.innerHTML = "Must Login first!";
    }else{
      displayBox2.innerHTML = "Enter Amount to Transfer: ";
      if (nam === "save"){
        state = 3;
      }
      else if (nam === "cheque"){
        state = 4;
      }
    }
    
  }
  const logout = () => {
    const buttons = document.querySelectorAll('.button3');
    buttons.forEach(button => {
      button.style.backgroundColor = '#004c9b';
    }); 
    const displayBox2 = document.getElementById("display-box-2");
    displayBox2.innerHTML = "Thanks for banking!";
    state = 0;
    loggedin = false;

  }
  const act = (nam) => {
    const buttons = document.querySelectorAll('.button3');
    const button = document.getElementById(nam);
    buttons.forEach(button => {
      button.style.backgroundColor = '#004c9b';
    }); 
    button.style.backgroundColor = 'red';
    const displayBox2 = document.getElementById('display-box-2');
    if (!loggedin) {
      displayBox2.innerHTML = "Must Login first!";
    }
    else{
      fetch('/account', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: nam })
      })
      .then(response => response.json())
      .then(data => {
        const displayBox2 = document.getElementById('display-box-2');
        displayBox2.innerHTML = data.result;
        displayBox2.style.color = 'black'; 
      })
      .catch(error => {
        console.error(error);
      });
  }
  }

  return (
    <div className = "App">
      <body>
        <nav class= "navbar">
        <div class="navbar-content">
          <span class="navbar-text">BIG BANK ATM</span>
          </div>
        </nav>
        <h1>
          BIG BANK!!
        </h1>
        <div class = "container">
          <div id = "displayTest">
            Welcome to BIG Bank! <br>
            </br> 
            Enter Card Number Here:
          </div>
             
          <input type="text" id="myInput"></input>

          <div class="display" className="display" id="display-box"></div>
          <br>
          </br>
          <button className="button" onClick={() => displayButtonNumber(1)}>1</button>
          <button className="button" onClick={() => displayButtonNumber(2)}>2</button>
          <button className="button" onClick={() => displayButtonNumber(3)}>3</button>
          <br></br>
          <button className="button" onClick={() => displayButtonNumber(4)}>4</button>
          <button className="button" onClick={() => displayButtonNumber(5)}>5</button>
          <button className="button" onClick={() => displayButtonNumber(6)}>6</button>
          <br></br>
          <button className="button" onClick={() => displayButtonNumber(7)}>7</button>
          <button className="button" onClick={() => displayButtonNumber(8)}>8</button>
          <button className="button" onClick={() => displayButtonNumber(9)}>9</button>
          <button class="button" onClick={() => clearDisplay()}>Clear</button>
          <button class="button" onClick={() =>  displayButtonNumber(0)}>0</button>
          <button class="button" onClick={() => submit()}>Submit</button>
          <div>{submitResult}</div>
        </div>
        <div class="container2">
        <div class="display2" id="display-box-2">
        </div>
        </div>
        <div class="container3">
          <button className="button3" id="deposit"onClick={() => deposit('deposit')}>Deposit Cash</button>
          <button className="button3" id="withdraw"onClick={() => withdraw("withdraw")}>Withdraw Cash</button>
          <br></br>
          <button className="button3" id="Chequing"onClick={() => act('Chequing')}>Chequing Balance</button>
          <button className="button3" id="Savings"onClick={() => act('Savings')}>Savings Balance</button>
          <button className="button3" id="save"onClick={() => transfer("save")}>Transfer to Savings</button>
          <button className="button3" id="cheque"onClick={() => transfer("cheque")}>Transfer to Chequing</button>
          <br></br>
          <button className="button4" id="log"onClick={() => logout()}>Logout</button>
          
        </div>
        
      </body>



    </div>
  )
}

export default App
