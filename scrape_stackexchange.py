import requests
from bs4 import BeautifulSoup
import csv

# specify the URL of the webpage to scrape
url = "https://stackexchange.com/"

# send a GET request to the specified URL
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find all the top questions on the page
questions = soup.find_all("a", class_="question-link")

# create a list to store the question topics, question contents, and tags
data = []

# loop through each question and extract its topic, content, and tags
for question in questions:
    # extract the topic of the question
    topic = question.get_text()
    # strip topic
    topic = topic.strip()
    # extract the URL of the question page
    question_url = question["href"]
    # send a GET request to the question page
    question_response = requests.get(question_url)
    # parse the HTML content using BeautifulSoup
    question_soup = BeautifulSoup(question_response.content, "html.parser")
    # extract the content of the question
    content = question_soup.find("div", class_="js-post-body").get_text().strip()
    # extract the tags of the question
    tags = question_soup.find_all("a", class_="post-tag")
    # print(tags)
    tag_list = [tag.get_text() for tag in tags]
    # remove duplicates from tag_list
    tag_list = list(set(tag_list))
    # add the topic, content, and tags to the data list
    data.append([topic, content, ", ".join(tag_list)])

# write the data to a CSV file
with open("stackexchange_top_questions.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Question Topic", "Question Content", "Tags"])
    writer.writerows(data)