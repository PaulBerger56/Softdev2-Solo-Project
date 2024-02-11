# Automated Birthday Emailer
### !!! IMPORTANT NOTE: IF YOU ADD YOUR GMAIL PASSWORD TO THIS PROJECT SET YOUR REPO TO PRIVATE !!!
Rewritten by Paul Berger.  Original Code from "100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu Day 32<br>
* Link to course: https://www.udemy.com/course/100-days-of-code/?kw=100+days+of+code&src=sac<br><br>

### Major Changes
* *passwd.py added rather than keeping Google Password in main.py*
* *Original project did not have automation,  would only work when run*
* *Added functionality to read in the entire letter_templates directory rather than manually typing out every line*
* *Added funtionality to replace the User's name in the letter templates*


### Getting Started
**These instructions assume that you already have python installed on your machine and are using VSCode as your IDE.**

1. When prompted, run the python code in a Python Virtual Environment.  This will make managing dependencies with pip freeze easier later on.
    - If you are not prompted to create a virtual environment, you can do it manually. 
    - In the bottom right of the VSCode screen, you will see an area that says "Python", click on the text just to the right of that.<br><br> ![Screenshot of VSCode](readme_images/VSCode.PNG)  <br> <br> 
    - This will bring up options at the top of the screen.  Click on "Create Virtual Environment"<br><br> ![Create Virtual Environment](readme_images/ve.PNG)<br><br>
2. If you try to run the code, you will get an error that pandas is not installed. <br><br> ![No module Pandas](readme_images/Pandas.PNG)<br><br>
    - To rectify this, we need to install pandas from the command line.
    - In the open terminal type "pip install pandas" and press enter.
    - Try running the code again.  If no errors pop up, you have all of the dependencies installed.  If you get a message about another missing dependency, do the same thing as the previous step, but replace pandas with the name of the missing dependency.

