# GUI Function Plotter 

## Description 
This project is a mathematical function plotter developed with PySide2 and Matplotlib. 

## Using this project  
First clone the repo using 
```
git clone https://github.com/AI091/Function_Plotter.git
```
Then go into the directory 
```
cd <local_repo_dir>
```
Then install the dependencies using 

```
pip install -r requirements.txt
```

## Working examples
Listed below are examples of correct input with their corresponding output 
<p align="center">
    <img 
        src= ./valid_example1.JPG
        alt = "x^2"
        title = "plot of x^2" 
    >
    <img 
        src= ./valid_example2.JPG
        alt = "3*x+1"
        title = "plot of 3*x+1" 
    > 
    <img 
        src= ./valid_example3.JPG
        alt = "x^4 +3*x^2 + 1/x"
        title = "plot of x^4 +3*x^2 + 1/x" 
    > 
</p>

## Wrong examples 
Demonstrated below is some wrong input with their corresponding error messages 

<div align="center">
<br>
<h3> Using Y which is not a supported operand </h3>

<p >
    <img 
        src= ./wrong_example1.JPG
        alt = "wrong_example1"
        title = "wrong_example1" 
    >
</p>
<br>

<h3>Empty Input </h3> 
<p >
    <img 
        src= ./wrong_example2.JPG
        alt = "wrong_example2"
        title = "wrong_example2" 
    > 
</p>
<br>

<h3> Invalid Mathematical expression</h3>
<p >
    <img 
        src= ./wrong_example3.JPG
        alt = "wrong_example3"
        title = "wrong_example3" 
    >
</p>
<br>

<h3> Min larger than max </h3>
<p >
    <img 
        src= ./wrong_example4.JPG
        alt = "wrong_example4"
        title = "wrong_example4" 
    >
</p>
<br>

</div>


# Project Layout
```
└── Function_Plotter
   ├── app.py
   ├── canvas.py
   ├── config.py
   ├── custom_errors.py
   ├── function_input.py
   ├── helper.py
   ├── test.py
   ├── requirements.txt
   ├── pytest.ini

```

- **app.py** : defines the main window and runs the application .

- **canvas.py** : defines the plotting canvas .

- **config.py** : defines some plotting parameters like the number of points used for plotting .

- **custom_errors.py** : defines custom errors used in the project .

- **function_input.py** : defines the widget that takes the input function .

- **helper.py** : defines helper functions for parsing the input in a modular fashion .

- **test.py** : defines the automated tests for the functionality of the app's separate parts and end to end as a whole .

- **requirements.txt** : defines the required dependencies to install the project.

- **pytest.ini** : defines the required configuration for pytest to run the tests properly.

## Testing 

The project has automated tests defined in ``` test.py ``` that are written using pytest and pytest-qt . 
To run the tests : 
```
pytest test.py
```




   







