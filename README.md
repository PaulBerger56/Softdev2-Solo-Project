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
 Notice: If instructions below on running the code in a virtual environment gives you issues, just switch back to whichever environment runs the code for you.  This section is to make a later step easier, but may cause more problems than solutions. 

1. When prompted, run the python code in a Python Virtual Environment.  This will make managing dependencies with pip freeze easier later on.
    - If you are not prompted to create a virtual environment, you can do it manually. 
    - In the bottom right of the VSCode screen, you will see an area that says "Python", click on the text just to the right of that.<br><br> ![Screenshot of VSCode](readme_images/VSCode.PNG)  <br> <br> 
    - This will bring up options at the top of the screen.  Click on "Create Virtual Environment"<br><br> ![Create Virtual Environment](readme_images/ve.PNG)<br><br>
    - Click on Venv -> Delete and Recreate -> Pick your Python Version -> leave requirements.txt unchecked if the option pops up.
2. If you try to run the code, you will get an error that pandas is not installed. <br><br> ![No module Pandas](readme_images/Pandas.PNG)<br><br>
    - To rectify this, we need to install pandas from the command line.
    - In the open terminal type "pip install pandas" and press enter.
    - Try running the code again.  If no errors pop up, you have all of the dependencies installed.  If you get a message about another missing dependency, do the same thing as the previous step, but replace pandas with the name of the missing dependency.

### Changing Values in main.py
**The way this code is set up, we will be using a gmail account to send the emails.  There are ways to set this up for other types of email addresses, but for now we are sticking with gmail. If you would like to use a different email provider, you can look up what Mail Protocol they use and change line 59 accordingly.**

1. On line 5, replace [Your Name Here] with the name you would like to go by in your outgoing emails.  For example, my first name is Paul, so I would change '[Your Name Here]' to 'Paul'.<br><br> ![Your Name Here](readme_images/your_name_here.PNG) <br><br>
2. On line 61 and 62, replace [Your Email Here] with your gmail adress that you would like the emails to be sent from.  For example if my email address was test@gmail.com, I would change '[Your Email Here]' to 'test@gmail.com'.<br><br> ![Your Email Here](readme_images/your_email_here.PNG) <br><br>

### Adding Recipients to birthdays.csv
* The format of the csv file is name,email,month,day
* Do not remove the header from this file. The first line needs to say name,email,month,day
* You can add as many recipients as you want to this file.
* Make sure there is only One recipient per line, and no spaces in between the values, only commas.
* It is okay to have spaces in the Name ex. 'Sue Ann'
* The email adress for the recipients can be any working email provider.  Only the outgoing email adress from the previous step needs to be gmail in this example.<br><br> ![birthdays.csv](readme_images/recipients.PNG) <br><br>

