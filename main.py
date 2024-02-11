import smtplib, datetime as dt, random, pandas, os
from passwd import PASSWORD

#Set the name to what you would like to go by on the outgoing emails
user_name = 'Paul'

# Get the current date 
birthdays_dict = {}
now = dt.datetime.now()
current_month = now.month
current_day = now.day

# Reads in the Birthday data from the csv file
data = pandas.read_csv("birthdays.csv")

# This line does the entire commented out for loop below in one line.  This is Dictionary Comprehension
birthdays_dict = {(row['month'], row['day']): row.to_dict() for _, row in data.iterrows()}

# birthdays_dict = {}

# for _, row in data.iterrows():
#     key = (row['month'], row['day'])
#     value = row.to_dict()
#     birthdays_dict[key] = value

# Sets the path to where the letters are
letter_directory = "letter_templates/"

letters = []

# Goes through all of the files in letter_templates and reads in the data
for filename in os.listdir(letter_directory):
    if filename.endswith(".txt"):  # Ensure we're only reading .txt files
        file_path = os.path.join(letter_directory, filename)  # Construct the full file path
        with open(file_path, 'r') as file:
            letters.append(file.read())


# Sees if the current date is in the birthdays_dict
check_key = (current_month, current_day)
if check_key in birthdays_dict:
    value = birthdays_dict[check_key]
    
    # Gets the values for the correct person and drafts the message
    name = value['name']
    email = value['email']    
    message = random.choice(letters)
    message = message.replace("[NAME]", name).replace("[USER]", user_name)        
    
    final_message = f"Subject:Happy Birthday!\n\n{message}"
    ''' 
    The final_message is formatted like this to create a Subject separate from the message itself.
    The format is Subject:[Subject Text Here]\n\n\n
    Replace [Subject Text Here] with the text you want and no brackets.
    The three escapes are important to make this work properly.
    '''
    
    # Sends the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user='paulberger56@gmail.com', password=PASSWORD)
        connection.sendmail(from_addr='paulberger56@gmail.com', 
                            to_addrs=email,
                            msg=final_message)
    
    


    







