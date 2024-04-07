# Flask Web Application Server COP4635 Sys & Net II Project 3

## OVERVIEW

This project aims to showcase effective HTTP method handling, specifically focusing on GET and
POST requests, using the Python Flask web framework. The goal was to create a straightforward
web calculator application that receives mathematical expressions (text) from users and
computes the results upon clicking the 'Calculate' button. Additionally, users are able to view 
the history of all calculations performed from the release of the
web application.
Furthermore, the server features an API (with endpoint ‘api/history’) for the calculation history,
presenting information in JSON format. 
This API serves both a web browser client and lays the foundation for a future programmatic client. 
The project provides a practical demonstration of serving web pages,
handling errors, and creating APIs using Flask.

## ENVIRONMENT

1. Python >= 3.8 
2. Flask == 3.10.12 (latest as of this project was developed), Project works in a  virtual enviornment.

## Running

To run the program, navigate into the calculator directory. From here, you may run the command
```
python server.py
```
and the server will start.

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


