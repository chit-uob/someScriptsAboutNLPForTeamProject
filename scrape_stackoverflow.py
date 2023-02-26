import requests
from bs4 import BeautifulSoup
import csv

# specify the URL of the login page
login_url = "https://stackoverflow.com/users/login"

# create a session object to persist the login session
session = requests.Session()

# send a GET request to the login page to get the login form
response = session.get(login_url)
soup = BeautifulSoup(response.content, "html.parser")
form = soup.find("form", id="login-form")

# extract the necessary form data from the login form
form_data = {}
for input in form.find_all("input"):
    if input.get("name") and input.get("value"):
        form_data[input["name"]] = input["value"]

# update the form data with your login credentials
form_data["email"] = ""
form_data["password"] = ""

# send a POST request to the login page with the form data
response = session.post(login_url, data=form_data)

# check if the login was successful
if "logout" not in response.url:
    print("Login failed")
else:
    print("Login successful")

# specify the URL of the webpage to scrape
url = "https://stackoverflow.com/"

# send a GET request to the specified URL using the logged-in session
response = session.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find all the top questions on the page
questions = soup.find_all("div", class_="question-summary")

# create a list to store the question topics, question contents, and tags
data = []

# loop through each question and extract its topic, content, and tags
for question in questions:
    # extract the topic of the question
    topic = question.find("a", class_="question-hyperlink").get_text()
    # extract the URL of the question page
    question_url = "https://stackoverflow.com" + question.find("a", class_="question-hyperlink")["href"]
    # send a GET request to the question page using the logged-in session
    question_response = session.get(question_url)
    # parse the HTML content using BeautifulSoup
    question_soup = BeautifulSoup(question_response.content, "html.parser")
    # extract the content of the question
    content = question_soup.find("div", class_="js-post-body").get_text().strip()
    # extract the tags of the question
    tags = question_soup.find_all("a", class_="post-tag")
    tag_list = [tag.get_text() for tag in tags]
    # add the topic, content, and tags to the data list
    data.append([topic, content, ", ".join(tag_list)])

# write the data to a CSV file
with open("stackoverflow_top_questions.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Question Topic", "Question Content", "Tags"])
    writer.writerows(data)
