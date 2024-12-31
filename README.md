# TMU Big Bank

The **TMU Big Bank Project** is an online ATM banking system that simulates key banking functions such as login, deposit, withdrawal, and account transfers. The project is built with the goal of demonstrating software engineering principles in a real-world context. This system mimics a real-world ATM, but is not intended for actual banking or sensitive data handling.

## Features

- **User Authentication**: Secure login for users to access their accounts.
- **Deposit/Withdrawal**: Users can deposit and withdraw funds from their accounts.
- **Account Transfer**: Allows users to transfer money between accounts.
- **Transaction History**: Displays a log of recent transactions for each user.

## Technologies Used

- **Frontend**:  
  The user interface is built using **React.js**, providing a dynamic and responsive experience. It allows users to interact with the system seamlessly and securely.

- **Backend**:  
  The backend of the system is powered by **Python** and the **Flask** framework. Flask is used to process banking operations, including deposits, withdrawals, and transfers, and to manage communication between the frontend and the database.

- **Database**:  
  Data is stored in **MySQL**, which ensures secure and reliable handling of user accounts and transaction data.

## Development Methodology

Out team focused on developing this project with the following **Spiral Development Methodology**, which emphasizes iterative cycles of planning, risk analysis, development, and testing. This allowed the project to evolve gradually, with frequent refinements, ensuring the system is robust, scalable, and functional.

## Setup and Installation

To get the **Big Bank Project** running on your local machine, follow these steps:

### 1. Clone the Repository
First, clone this repository to your local machine

### 2. Install Dependencies
- Ensure that Python and Node.js are installed on your system.
- Install dependencies for both frontend (React) and backend (Flask) components by navigating to the respective directories and running ```npm install and pip install -r requirements.txt.```

### 3. Set Up MySQL Database
- Install and configure the MySQL server on your system.
- Create a database and update the credentials as per the SQL README file.

### 4. Start the Backend
In the backend directory, run the appropriate command to start the Flask server.

### 5. Launch the Frontend
In the frontend directory, start the React development server using the command provided.

### 6. Access the Application
Open a browser and navigate to the local address provided to begin interacting with the ATM system.

## Note!
- This project is for educational purposes and should not be used for actual banking or handling sensitive financial data.
- Data stored in the MySQL database is not persistent across different sessions, so for demo purposes, you may need to reset the database or re-enter information.