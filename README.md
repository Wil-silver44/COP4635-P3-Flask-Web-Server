# Flask Web Application Server COP4635 Sys & Net II Project 3

## OVERVIEW

This project aims to showcase effective HTTP method handling, specifically focusing on GET and
POST requests, using the Python Flask web framework. The goal is to create a straightforward
web calculator application that receives mathematical expressions (text) from users and
computes the results upon clicking the 'Calculate' button. Additionally, you'll implement a
feature allowing users to view the history of all calculations performed from the release of your
web application (you might have restarted your server several times but the user should be able
to see all calculations performed when the server is up and running). The history page should
provide an option to go back to calculator page(home). The historical data will be stored in a
text file acting as the database.
As part of the project, you'll develop a Flask web server with the mentioned functionalities. This
server will also handle the HTTP error '404' gracefully, presenting a customized message and a
link back to the home page. This process will illustrate how to serve various web pages (HTML
pages and routes) to clients, specifically web browsers.
Furthermore, you'll create an API (with endpoint ‘api/history’) for the calculation history,
presenting information in JSON format (see attached output screenshot for the structure of
json). This API serves both a web browser client and lays the foundation for a future
programmatic client. The project provides a practical demonstration of serving web pages,
handling errors, and creating APIs using Flask.

## ENVIRONMENT

1. Python >= 3.8 and Flask == 3.0.2 (latest as of this project was created) , it is
recommended to work on your project by creating python virtual environment.

## IMPLEMENTATION

Program the web server in python using flask framework. The server will listen on a valid port.
Make sure you use a port number from the valid port number range (60001 – 60099) if you use
CS department’s SSH server, you may use any available port (ex: 8080, 8000, 5000) if you are
running on your machine. When client (browser) request for an html file (route) that does not
exists at the server, then your server should respond with small, but descriptive error message
and link to home page of your application that should be received by the client and displayed.
Your HTTP server should be verbose, and display all activity going on at the server.
Your server should respond to any standard browser program that is chosen to run as the client.
If a user makes a request for the HTML page files while the server is running, the server should
send the file to the browser if the request is valid. In case of the valid request/s the browser
would receive the HTML file and display it on the screen. Make sure that your HTTP server
program does not exit unless forced by the tester to stop. The server program should be coded
by you so as to let the user perform more calculations in the same way through the browser
client, and not exit immediately.

# PROJECT FOLDER STRUCTURE AND FILES
![image](https://github.com/Wil-silver44/COP4635-P3-Flask-Web-Server/assets/89366767/4318852f-7080-4869-af62-914bb2b4e8ed)

• Calculator --- to store all the files related to this project
  o Templates --- folder to store all html files (flask uses jinja template format)
▪ 404.html --- to customize ‘not found error message’ and add link to home page
▪ calculator.html --- index (or home) page for your application
▪ history.html --- this is used to display the list of calculations performed
  o data
▪ calculation_history.txt --- to store the calculations performed in a file
  o requirements.txt --- specify the python dependencies for your project (here you should add flask dependency as “Flask==3.0.2”)
  o server.py --- your server program and main logic goes here
  o README --- contains names of all project members, directions on running your code indicating usage and examples, python and flask versions 
  and any other relevant details like an analysis if project wasn’t completed, and what part was accomplished.
  o screenshots --- folder to store all your screenshots of the features you implemented


