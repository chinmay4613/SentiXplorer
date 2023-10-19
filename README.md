# SE Project 2- Group 22

# C.E.L.T: The Sentimental Analyser 

### YouTube Link: 

[Video link](https://www.youtube.com/watch?v=bRi_v8ERdq4&ab_channel=rushilpatel)

[![DOI](https://zenodo.org/badge/703204680.svg)](https://zenodo.org/doi/10.5281/zenodo.10015848)

[![Build Status](https://travis-ci.org/bsharathramesh/SE_Project1.svg?branch=master)](https://travis-ci.org/bsharathramesh/SE_Project1)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

 [![codecov](https://codecov.io/gh/MuskKat/SE_Project1/branch/main/graph/badge.svg)](https://codecov.io/gh/MuskKat/SE_Project1)


## INTRODUCTION

Sentiment analysis is one of the fastest growing research areas in computer science, making it challenging to keep track of all the activities in the area. In our project we aim to achieve our goal in accurately predicting a users sentiment by analysing the data provided in any of the five different methods. They are Document Analysis, Comment Analysis, Text Analysis, Product Analysis and Audio Analysis. This project though currently in the initial stages of development, can be further applied to numerous domains which can be useful for the society. This document provides a major perspective for the users to understand and take up the project as an Open source software and add on multiple features before releasing to the market. Also, the document aids the developers in understanding the code and acts as a reference point for starting the project.

The complete development was achieved using the following technologies and it is recommended that the next set of developers who take up this project have these technologies installed and keep them running before proceeding further:

Python3 <br>
Django <br>
HTML<br>
CSS<br>
Scrappy<br>
Vader Analysis Tool

Although we have used HTML and CSS for the FrontEnd, the users can merge the backend logic with any of the front end frameworks they wish to use such as React, angularJS, etc.


## Steps for execution
1. Run `pip install -r requirements.txt` followed by `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"`. If there are any additional prerequisite modules that your PC system lacks, please run `pip install "insert-module-name"`.
2. Make sure you change the path accordingly in the files.  (Refer to the issue: https://github.com/bsharathramesh/SE_Project1/issues/31 to get the list of files where changes are needed)
3. Execute manage.py using the command `python3 manage.py runserver` at `/SE_Project1/sentimental_analaysis`. This runs the Django server such that we can open the webUI for the project on the browser.
4. Next, open your browser and type in `localhost:8000` in the search bar to open the webUI of the application.
5. The UI typically looks as shown below and here you have a choice between URL, file or normal text input.

When you first run the files, you are asked to log in or register yourself. 

![First](https://github.com/MuskKat/SE_Project1/blob/master/screenshots/user_login_page.png)
![orthen](https://github.com/MuskKat/SE_Project1/blob/master/screenshots/user_signup_page.png)

After logging in, here's the landing page of the Sentiment Analyzer.

![second](https://github.com/MuskKat/SE_Project1/blob/master/screenshots/user_homepage.png)

The UI for URL input for product analyzis is as shown below:

![product](https://github.com/MuskKat/SE_Project1/blob/master/screenshots/amazon_product_analysis.png)

The UI for file input for document analysis is as shown below:

![docum](https://github.com/MuskKat/SE_Project1/blob/master/screenshots/document_analysis.png)

The UI for text input for text analysis is as shown below:

![text](https://github.com/MuskKat/SE_Project1/blob/master/screenshots/text_analysis.png)

The UI for audio input for audio analysis is as shown below:

![audio](https://github.com/MuskKat/SE_Project1/blob/master/screenshots/audio_analysis_page.png)

The UI for URL input for comment analysis is as shown below:

![ytanal](https://github.com/MuskKat/SE_Project1/blob/master/screenshots/youtube_comments_analysis.png)

The Output as below:

![output](https://github.com/MuskKat/SE_Project1/blob/master/screenshots/analysis_bar_graph.png)
![out](https://github.com/MuskKat/SE_Project1/blob/master/screenshots/analysis_pie_chart.png)

## Case Study: Amazon Product Review Sentiment and Text Analysis

### WordCloud of Reviews
![wc](https://user-images.githubusercontent.com/9015214/97310439-9e1f8380-1839-11eb-8060-0944d7e4d7d9.png)

### Reviews Summary
<img width="896" alt="Screen Shot 2020-10-27 at 9 49 08 AM" src="https://user-images.githubusercontent.com/9015214/97310491-aaa3dc00-1839-11eb-97ef-e2e27fd6fad2.png">

### Sentiment Summary
<img width="864" alt="Screen Shot 2020-10-27 at 9 48 02 AM" src="https://user-images.githubusercontent.com/9015214/97310362-834d0f00-1839-11eb-97db-f32a3d1f9eed.png">

### Confusion Matrix
![conf](https://user-images.githubusercontent.com/9015214/97310260-631d5000-1839-11eb-9a3b-102fa9737439.png)



## FUTURE SCOPE

Store history for each user and the corresponding analysis results.

Recommendation system based on analysis results.

Live speech to text sentiment analysis.

Enhance the analysis by taking into consideration the number of users rated for each product.

Extend the developed Youtube comment analysis to Facebook, Twitter and LinkedIn Posts.

Audio diarization to split input audio in sections according to different speakers, to analyse individual speaker sentiment.


## Team Members

Rucha Mahesh Kulkarni

Muskan Katoch

Mihir Nikam

Rushil Patel
				

