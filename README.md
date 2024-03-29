# Automated Birthday Emailer
### !!! IMPORTANT NOTE: IF YOU ADD YOUR GMAIL PASSWORD TO THIS PROJECT SET YOUR REPO TO PRIVATE !!!
Written by Paul Berger.  Inspired by the Birthday Emailer project from "100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu Day 32<br>
* Link to course: https://www.udemy.com/course/100-days-of-code/?kw=100+days+of+code&src=sac<br><br>

### Major Changes
* *passwd.py added rather than keeping Google Password in main.py*
* *Original project did not have automation,  would only work when run*
* *Added functionality to read in the entire letter_templates directory rather than manually typing out every line*
* *Added funtionality to replace the User's name in the letter templates*

### Creating and pushing code to a private Github Repository
**!!! If you are forking this code from my repo, make sure to save it and upload it to a new repository so that you can make it Private. Don't forget to delete the .git folder after copying it. At this time, there is no option to make a fork Private !!!  <br><br>
There is sensitive information in this project including your personal gmail account name and the special password you created.  Because of this, we want to make sure that the repository is set to private.  While it is unlikely that anyone will be finding our repositories and taking our information, it is not impossible.  You never know who has web scrapers looking all over the place for information like this.  It is better to be safe than sorry! Setting the repository to private means that only the owner and anyone they set as a contributor can see the it**
1. Navigate to your github page and go to your Repositories.  Once there, click 'New' in the top right.<br><br> ![New Repository](readme_images/repos.PNG) <br><br>
2. Name your Repository something relevant and add a Description if you would like.  Just under Description, make sure the Satellite button next to 'Private' is Selected.  Make sure that the checkbox next to 'Add a README file' is UNCHECKED!!!!  There will be a conflict between this readme and the one you made if you leave that box checked.<br><br> ![Create a new Repo](readme_images/createANewRepo.PNG) <br><br>
3. Scroll down to the bottom of the page and click the 'Create repository' button.<br><br> ![Create Button](readme_images/createButton.PNG) <br><br>
4. Now you will be brought to the homepage of the new repository, but it will be completely empty.  Scroll down to the 'Quick setup' section and look for '...or push an existing repository from the command line'.  Click on the little boxes in the top right of the code just below it to copy the contents, or highlight the contents and press copy.<br><br> ![push an existing repo](readme_images/quickSetup.PNG) <br><br>
5. Open your project in VSCode and make sure 'Birthday Wisher is the Root folder'.  Click on 'Terminal' at the top of the page and in the dropdown click 'New Terminal'.  If you would prefer to open a git bash in the root folder of the project in your file explorer, that is fine too.<br><br> ![New Terminal](readme_images/newTerminal.PNG) <br><br>
6. In the terminal, or in your git bash, type "git init" without the quotation marks and press enter.
7. Once the local repository is initialized you need to add and commit the local code before being able to push.
    * Type "git add ." without the quotation marks and press enter
    * Type "git commit -m 'Initial Commit' " without the quotation marks and press enter.
8. Paste the commands you copied from the '...or push an existing repository from the command line' section and press enter. 
**!!!It is assumed that you have all of your credentials set up already.  If they are not, you may have to temporarily revert the repository back to public, remove any passwords or email addresses from your code, push the code to the repository, and set the repository back to private. Then return any passwords and email adresses to the code. If this is the case, I recommend completing all other steps up through testing that the code works before pushing to the repo.!!!**<br><br> ![Pasting Commands](readme_images/terminalCommands.PNG) <br><br>
9. Go back to your github repository's homepage and refresh.  If everything went well, you should see your code here.<br><br> ![Uploaded Properly](readme_images/uploadedProperly.PNG) <br><br>


### Getting Started
**These instructions assume that you already have python installed on your machine and are using VSCode as your IDE.**
 **!!! Notice: If the instructions below on running the code in a virtual environment gives you issues, just switch back to whichever environment runs the code for you.  This section is to make a later step easier, but may cause more problems than solutions You will still need to install any missing dependencies!!!** 

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

1. On line 5, replace [Your Name Here] with the name you would like to go by in your outgoing emails.  For example, my first name is Paul, so I would change '[Your Name Here]' to 'Paul'. ex: user_name = 'Paul'<br><br> ![Your Name Here](readme_images/your_name_here.PNG) <br><br> ![Paul](readme_images/paul.PNG) <br><br>
2. On line 61 and 62, replace [Your Email Here] with your gmail adress that you would like the emails to be sent from.  For example if my email address was test@gmail.com, I would change '[Your Email Here]' to 'test@gmail.com'. ex: user='test@gmail.com'<br><br> ![Your Email Here](readme_images/your_email_here.PNG) <br><br> ![testmail](readme_images/testmail.PNG) <br><br>

### Adding Recipients to birthdays.csv
* The format of the csv file is name,email,month,day
* Do not remove the header from this file. The first line needs to say name,email,month,day
* You can add as many recipients as you want to this file.
* Make sure there is only One recipient per line, and no spaces in between the values, only commas.
* It is okay to have spaces in the Name ex. 'Sue Ann'
* The email adress for the recipients can be from any working email provider.  Only the outgoing email adress from the previous step needs to be gmail in this example.<br><br> ![birthdays.csv](readme_images/recipients.PNG) <br><br>

### Adding more letter templates
**You can add as many letter templates as you want in this project.  If the code detects a birthday, one will be chosen randomly and sent to the recipient.**
* The files must be in the .txt format.<br><br> ![Letters](readme_images/letters.PNG) <br><br>
* For the code to add your name as the sender, and the recipients name properly, you must use the proper format. 
    * Use the token [NAME] for the recipient's name.
    * Use the token [USER] for the sender's name.
    <br><br> ![Letters](readme_images/user.PNG) <br><br>
* If done correctly, lines 45 to 48 in main.py will replace them with the proper names. <br><br> ![Replace](readme_images/replace.PNG) <br><br>

### Creating and retrieving a password from Google
**Google creates special passwords to be able to send emails from your code rather than directly from your gmail page.  If you are using a different email service, you will have to look up how to do this part with their available services.  We will copy the password that is generated and put it in our passwd.py file.**
1. Go to google.com and click your profile picture in the top right and in the dropdown box click 'Manage your Google Account'.<br><br> ![Google Homepage](readme_images/google.PNG) <br><br>
2. On the left side of the Screen, click Security.<br><br> ![Security](readme_images/security.PNG) <br><br>
3. Scroll down to the Section labeled 'How you sign in to Google' and click on 2-Step Verification.<br><br> ![2-Step](readme_images/2Step.PNG) <br><br>
4. If prompted to enter your password, go ahead and do so. Once on the 2-Step Verification Page, scroll all the way down to the section Labeled 'App Passwords' and click on the little arrow on the right side of the box.<br><br> ![App Password Section](readme_images/apppass.PNG) <br><br>
5. Once on the App passwords page, type a relevant name that pertains to this project in the App name text box and click create. Try to be specific with this name so you remember what project the password goes with.<br><br> ![Create App Password](readme_images/createAppPass.PNG) <br><br>
6. __IMPORTANT!!! DO NOT SHARE THIS PASSWORD WITH ANYONE. MAKE SURE YOUR REPOSITORY IS SET TO PRIVATE BEFORE PUSHING THE CODE TO IT WITH THIS PASSWORD IN IT!!!__
A pop up box will appear with your password showing.  It would be a good idea to save this password in a txt file or some other file locally, but outside of your project.  Once you leave this pop up window, you will not be able to access the code again.  If you lose it, you will have to create a new one and use that.<br><br> ![Password](readme_images/password.PNG) <br><br>
7. Copy this code and open passwd.py. Once there, replace [Your password here] with the password you just copied.  For example, I would change PASSWORD = "[Your password here]" to PASSWORD = "111 awsdgt 33asda". FYI this is a fake example.<br><br> ![Password Equals](readme_images/passwordEquals.PNG) <br><br>

### Testing the code
**Now that we have done all the steps to set up the code with our email, it is time to test it to make sure it works.  We will do this by sending an email to ourselves using the current date.**
1. Go into the birthdays.csv file and create a new entry with whatever name you want, an email address that you have access to, and the current date.<br><br> ![Password Equals](readme_images/todayTester.PNG) <br><br>
2. Go to your browser and open the inbox of the email address that you put in the birthdays.csv file with the current date.  If everything is set up properly, you will see an email created from one of the letter templates with the proper names included.  <br><br> ![Recieved Email](readme_images/emailWorked.PNG) <br><br>
3. If you recieved your email, everything is set up properly and you are ready to move on to automating the process.  If you did not recieve the email, first check to make sure that it did not end up in a spam folder.  If you still do not see it anywhere, go back through the steps and make sure you have everything formatted correctly and are using the same gmail account that you set up the special password for.





### Starting the Automation Process
**Assuming that that previous steps went well, and you recieved the email from yourself, you are ready to move onto the autmation process.  For this, we are going to use a feature that is built into github called github actions.  It is free up to a certain threshold per month, but if this is the only program you are running, and assuming you set things up correctly, you will remain in the free tier.  To make sure the recipients see the email on their actual Birthday, we will schedule it to run early in the morning.**
1. If you have not pushed the changed code to your repository, go ahead and do so now.
2. Navigate to your repository's homepage and click on 'Actions' in the top bar. Once on the Actions page, click on 'set up a workflow yourself'.  Just below, github has a lot of premade actions, but in this case we are going to make our own.<br><br> ![Actions Page](readme_images/actionsPage.PNG) <br><br>
3. As you can see, this will create a new file structure that we will need to automate our code.  This page will also have a large empty text field which is an empty main.yml file.  The .yml file is where we put the commands to let github know how and when to run our code. You can edit the code here, but I recommend pressing 'Commit changes' in the top right and pulling this file and file structure to your local repository and editing it in your IDE. To do this, either in the terminal of your IDE, or your git bash shell, type "git pull" without the quotation marks and press enter.<br><br> ![Empty YML](readme_images/emptyYML.PNG) <br><br>
4. In your IDE you will see the new directories .github\workflows with the main.yml file there.  Go ahead and open main.yml.  If it is giving you an error, that is okay.  It is most likely just because the file is currently empty.<br><br> ![IDE YML](readme_images/newFileStructure.PNG) <br><br>
5. For now I am going to give you the code for this in the actions.txt file located in the project, but explain what each part does. Go ahead and copy the contents from actions.txt into main.yml.  Feel free to delete actions.txt once this step is complete. P.S. If main.yml gives you an error when you paste the code in, it is okay.  For some reason VSCode doesn't understand yml.<br><br>
    * Line 1: This line is used to name the action.  You can change this to whatever you want, it is just a descriptor.  In this case, our action is running main.py, so it is named Run main.py<br><br> ![Run main.py](readme_images/runMain.PNG) <br><br>
    * Lines 3-5: Schedules when the code should be run. We use - cron tag with a cron expression on line 5.  This is an expression that covers a huge range of times in a small amount of text.  This is very hard to understand when first seeing it.  I recommend using chatgpt to ask how to cron schedule every day at 7 am, then checking that the code is correct at https://crontab.guru/<br><br> ![Cron](readme_images/cronYML.PNG) <br><br>
    * Lines 7-25: This is the jobs: section.  This is where we tell the actions exactly what we want done. Everything in the build: section will be run sequentially.<br><br> ![Jobs](readme_images/jobs.PNG) <br><br>
    * Line 9: runs-on: ununtu-latest Tells github that this code needs to be run on ubuntu linux.  There are other os options to run the code on as well.<br><br> ![runs-on](readme_images/runsOn.PNG) <br><br>
    * Lines 10 - 25: The rest of the lines are under the steps: subheader.  This just means that github should perform these actions sequentially.<br><br> ![steps](readme_images/steps.PNG) <br><br>
    * Lines 11-12: Names the step with 'name' and runs the action with 'uses'.  actions/checkout@v2 makes a copy of the code in the repo to use on the ubuntu server that was just started.<br><br> ![checkout](readme_images/checkout.PNG) <br><br>
    * Lines 14-17: Names the step with 'name', runs the action with 'uses', and sets the python version with 'with'.  This gets github to install python version 3.9 on the ubuntu server.<br><br> ![Setup Python](readme_images/pythonVersion.PNG) <br><br>
    * Lines 19-22: Names the step with 'name' and runs the action with 'run'. This gets github to install pip on the ubuntu server and install all dependencies with requirements.txt(We have not set this up yet, but will get to this part soon.)<br><br> ![Install Python Packages](readme_images/installPackages.PNG) <br><br>
    * Lines 24-25: Names the step with 'name' and runs the action with 'run'. This is the final step and runs main.py on the ubuntu server that was created.<br><br>![Execute py Script](readme_images/execute.PNG) <br><br>
6. Now that we have main.yml set up, we need to make sure we have our dependencies updated  into requirements.txt. This is the part that would be made easier if we used a virtual environment.  We are going to put all of our pip dependencies into a file so that github actions can install them on the server it creates.  If you successfully created a virtual environment, only the dependencies we need specifically for this project are installed, but if you have been using python for a long time and have installed dependencies, our requirements.txt will be bloated and will take longer to run inside of actions.  If this is the case, don't worry, I made a copy of only the dependencies we need and put it into short_requirements.txt.<br><br>
    * In the terminal of your IDE type "pip freeze > requirements.txt" without the quotation marks and press enter. This will create a file with all of our downloaded dependencies.<br><br> ![PIP freeze](readme_images/freeze.PNG) <br><br>
    * You should see that requirements.txt has been added to the file structure.<br><br> ![requirements](readme_images/requirementsTwo.PNG) <br><br>
        * If your requirements.txt looks short and with only a few entries like the image below, you should be fine and can delete short_requirements.txt.<br><br> ![normal requirements](readme_images/requirements.PNG) <br><br>
        * If your requirements.txt looks extremely long like the image below, go ahead and delete the contents from it.  Copy the contents of short_requirements.txt and paste them in requirements.txt.  Feel free to delete short_requirements after copying the contents over.<br><br> ![Too many requirements](readme_images/longRequirements.PNG) <br><br>
7. Once all of these steps have been completed, our code is ready to be sent to github.  Go ahead and type "git push" without the quotation marks into your terminal or git bash and press enter.

### Testing And finishing touches
**Now that we have set everything up, we want to make sure that the action works before leaving it to run on it's own.  We are going to test this by setting our cron expression to run every two minutes and make sure that we have our own email address as an entry in birthdays.csv.**

1. In your IDE go to main.yml and change the cron expression on line 5 to "*/2 * * * *".  This will set it to run every two minutes.<br><br> ![Two Minutes](readme_images/twoMinutes.PNG) <br><br>
2. In birthdays.csv make sure there is an entry with an email address that you have access to with the date set as the current date.  This should still be in our csv file from earlier, but if not, go ahead and add it now.<br><br> ![birthday.csv Test](readme_images/birthdayTest.PNG) <br><br>
3. Once both of those are set, go ahead and type "git push" without the quotation marks into your terminal and press enter. It may take some time for everything to get uploaded to github, so the code may not run right at the 2 minute mark.  
4. While you are waiting, go ahead and navigate to the Actions tab in your repository.  You will probably see a failed action here named Create main.yml.  There is no need to worry.  This is from when we created the empty .yml file earlier with no code inside of it.<br><br> ![Failed Action](readme_images/failedAction.PNG) <br><br>
5. After a few minutes, you should hopefully see at least one successful action named 'Run main.py' since that is what we named it in the .yml file.<br><br> ![Successful Action](readme_images/successfulActions.PNG) <br><br>
6. Go ahead and check the inbox of the email you used in birthdays.csv. 
    * If you see an email there from yourself, Pat yourself on the back!  You successfully set up Github Actions! All we need to do now is clean things up!
    * If you do not see an email there from yourself or you only have failed github actions, I have some bad news for you.  Something went wrong...  Go back through the steps and make sure you have everything set up and written properly.  It is easy to make a typo somewhere along the way.
7. Now we are on the cleanup step.  
    * Go into main.yml and revert the cron expression back to '0 7 * * *'<br><br> ![Cron Reverted](readme_images/cronReverted.PNG) <br><br>
    * Go into birthdays.csv and delete any tester entries that you made.  There should only be entries for actual potential recipients now.
    * If you still have short_requirements or actions.txt feel free to delete them from the project.

### Congratulations!!!  You succesfully deployed python code in Github Actions!!!<br><br> ![Congrats](readme_images/congrats.png) <br><br>
**If you have made it here, you have successfully deployed your first scheduled python code!!!  You can now leave it running in the background and you will never be accused of forgetting anyone's birthday ever again!  Just don't forget to add anyone!**

**Now that you have completed this, you will be able to create your own ideas and schedule them.  Try to think of other ideas you would like to have running in the background and create your own unique Programs!**

**Thanks for taking the time to go through my Walkthrough - Paul**