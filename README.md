# SentiXplorer
### *Insightful Analysis Beyond Words - Decode Emotions in Text, Audio, and More.*

<img src="https://github.com/chinmay4613/SentiXplorer/assets/56782318/9738b301-2545-41a7-b97a-59b9eef35792" alt="logo" width="350px"></img>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10023452.svg)](https://zenodo.org/doi/10.5281/zenodo.10023452)
[![GitHub Release](https://img.shields.io/github/release/chinmay4613/SentiXplorer)](https://github.com/chinmay4613/SentiXplorer/releases/tag/wolftrack)
[![codecov](https://codecov.io/gh/aniketdarp190301/WolfTrack4.0/graph/badge.svg?token=3OWJ1DERO5)](https://codecov.io/gh/aniketdarp190301/WolfTrack4.0)
![GitHub language count](https://img.shields.io/github/languages/count/chinmay4613/SentiXplorer)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/chinmay4613/SentiXplorer)](https://github.com/chinmay4613/SentiXplorer)
[![GitHub-size](https://img.shields.io/github/languages/code-size/chinmay4613/SentiXplorer)](https://github.com/chinmay4613/SentiXplorer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Video link](https://www.youtube.com/watch?v=bRi_v8ERdq4&ab_channel=rushilpatel)


## Introduction

In a world buzzing with digital conversations, deciphering the emotions hidden within text, audio, and various data sources is more critical than ever. Enter _SentiXplorer_ – your comprehensive solution for insightful analysis beyond words.

## Features


- **Document Analysis**:
Unlock deep insights and sentiments buried in lengthy documents, enabling users to swiftly navigate and understand the overarching sentiment and opinions conveyed in comprehensive textual data.

- **Text Analysis**:
From social media posts to customer reviews, SentiXplorer offers a meticulous examination of textual sentiments, facilitating a nuanced understanding of public perception for informed decision-making.

- **Facial Emotion Analysis**:
Ideal for marketing and user experience studies, this feature provides actionable insights into how visual content resonates emotionally, offering a deeper understanding of audience engagement.

- **Audio Analysis**:
Enhance customer support strategies by evaluating call center interactions, uncover sentiments in podcasts or interviews, and gain insights from audio content that may hold significant emotional cues.

- **Product Review Analysis**:
Identify product strengths and weaknesses, respond promptly to customer concerns, and refine product offerings based on real-time feedback to enhance overall customer satisfaction.

- **YouTube Comments Analysis**:
Gain a deep understanding of viewer sentiments, address concerns expressed in comments, and refine content strategies based on real-time feedback from one of the largest video-sharing platforms.

- **YouTube Video Analysis**:
Evaluate the impact of video content, refine content strategies based on viewer sentiments, and stay attuned to the dynamic landscape of YouTube for strategic content planning and optimization.

- **Reddit Topic Analysis**:
Understand the pulse of online communities, identify emerging trends, and gauge public sentiment on diverse subjects through detailed analysis of Reddit discussions.


## Tech Stack

<img src="https://github.com/chinmay4613/SentiXplorer/assets/56782318/b10dc1b9-c947-46f5-90c6-b010f6e4bcb6" alt="logo" width="450px"></img>



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



## Developer Support and Updates

For support and inquiries related to **SentiXplorer**, please contact us at **sentixplorer@gmail.com**. We are here to assist you and address any questions or issues you may have.

Stay Connected:

- **Discord Community**: Join our active Discord community at [https://discord.gg/sentixplorer](https://discord.gg/twPCh7AM) to engage with our team, ask questions, and stay up-to-date with the latest developments of the project.

We appreciate your interest and look forward to providing you with the best possible support and updates.

## :handshake: Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/shreyavaidya2311">Shreya Vaidya</a></td>
    <td align="center"><a href="https://github.com/Dhruv-Kolhatkar">Dhruv Kolhatkar</a></td>
    <td align="center"><a href="https://github.com/aniketdarp190301">Aniket Darp</a></td>
    <td align="center"><a href="https://github.com/chinmay4613">Chinmay Walinjkar</a></td>
  </tr>
</table>
				

