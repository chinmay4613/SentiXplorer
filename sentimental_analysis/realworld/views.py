from django.shortcuts import render, redirect, reverse
from django.core.files.storage import FileSystemStorage
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from django.template.defaulttags import register
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from youtube_transcript_api import YouTubeTranscriptApi
from io import StringIO
from .utilityFunctions import *
import os
import json
import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googleapiclient.discovery import build
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Analysis
from .signup import SignUpForm
from django.http import HttpResponse
from googleapiclient.discovery import build
from django.contrib.auth.decorators import login_required
from .utilityFunctions import detailed_analysis
import tweepy
import requests
import praw
import cv2 
import matplotlib.pyplot as plt 
from deepface import DeepFace 
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key, 0)


def index(request):
    print()
    if request.user.is_authenticated:
        return render(request, "realworld/index.html", {"current_user": request.user})
    else:
        return render(request, "realworld/index.html")


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'realworld/index.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def index1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if request.user.is_authenticated:
            context = {"current_user": request.user}
            return render(request, 'realworld/index.html', context)
        else:
            return render(request, 'realworld/index.html')
    else:
        return render(request, "realworld/index.html")


def pdfparser(data):
    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data = retstr.getvalue()

    text_file = open("Output.txt", "w", encoding="utf-8")
    text_file.write(data)

    text_file = open("Output.txt", 'r', encoding="utf-8")
    a = ""
    for x in text_file:
        if len(x) > 2:
            b = x.split()
            for i in b:
                a += " "+i
    final_comment = a.split('.')
    return final_comment


def analysis(request):
    return render(request, 'realworld/index.html')


def get_clean_text(text):
    text = removeLinks(text)
    text = stripEmojis(text)
    text = removeSpecialChar(text)
    text = stripPunctuations(text)
    text = stripExtraWhiteSpaces(text)

    # Tokenize using nltk
    tokens = nltk.word_tokenize(text)

    # Import stopwords
    stop_words = set(stopwords.words('english'))
    stop_words.add('rt')
    stop_words.add('')

    # Remove tokens which are in stop_words
    newtokens = [item for item in tokens if item not in stop_words]

    textclean = ' '.join(newtokens)
    return textclean


def detailed_analysis(result):
    result_dict = {}
    neg_count = 0
    pos_count = 0
    neu_count = 0
    total_count = len(result)

    for item in result:
        cleantext = get_clean_text(str(item))
        sentiment = sentiment_scores(cleantext)
        compound_score = sentiment['compound']

        pos_count += sentiment['pos']
        neu_count += sentiment['neu']
        neg_count += sentiment['neg']

    total = pos_count + neu_count + neg_count
    result_dict['pos'] = (pos_count/total)
    result_dict['neu'] = (neu_count/total)
    result_dict['neg'] = (neg_count/total)
    return result_dict


def get_face_analysis():
    # read image 
    img = cv2.imread('/Users/dhruvkolhatkar/Documents/Screenshots/happy.png') 
    result = DeepFace.analyze(img,actions = ['emotion'])
    print(result[0]['emotion']) 
    return result[0]['emotion']

@login_required(login_url="/login")
def faceAnalysis(request):
    if request.method == 'POST':
        file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(file.name, file)
        pathname = "media/"
        extension_name = file.name
        extension_name = extension_name[len(extension_name)-3:]
        path = pathname+file.name
        print(path)
        result = get_face_analysis()
        os.system(
            'cd /Users/sj941/Documents/GitHub/SE_Project1/sentimental_analysis/media/ && rm -rf *')
        return render(request, 'realworld/face_analysis_result.html', {"sentiment": result, "current_user":request.user})
    else:
        note = "Please enter the facial photo you want to analyze"
        return render(request, 'realworld/face_analysis.html', {'note':note, "current_user":request.user})

@login_required(login_url="/login")
def input(request):
    if request.method == 'POST':
        file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(file.name, file)
        pathname = "media/"
        extension_name = file.name
        extension_name = extension_name[len(extension_name)-3:]
        path = pathname+file.namexs
        result = {}
        if extension_name == 'pdf':
            value = pdfparser(path)
            result = detailed_analysis(value)
        elif extension_name == 'txt':
            text_file = open(path, 'r', encoding="utf-8")
            a = ""
            for x in text_file:
                if len(x) > 2:
                    b = x.split()
                    for i in b:
                        a += " " + i
            final_comment = a.split('.')
            result = detailed_analysis(final_comment)
        elif extension_name == 'wav':
            r = sr.Recognizer()
            with sr.AudioFile(path) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text)
                text = r.recognize_google(audio_data)
                value = text.split('.')
                result = detailed_analysis(value)
        print("YOLO",result)
        # Sentiment Analysis
        os.system(
            'cd /Users/sj941/Documents/GitHub/SE_Project1/sentimental_analysis/media/ && rm -rf *')
        return render(request, 'realworld/sentiment_graph.html', {'sentiment': result, "current_user": request.user})
    else:
        note = "Please Enter the Document you want to analyze"
        return render(request, 'realworld/documentanalysis.html', {'note': note, "current_user": request.user})


@login_required(login_url="/login")
def productanalysis(request):
    if request.method == 'POST':
        blogname = request.POST.get("blogname", "")
        text_file = open(
            "C:/Users/Rushil/Desktop/ncsu sem1/SE/New folder/SE_Project1/Amazon_Comments_Scrapper/amazon_reviews_scraping/amazon_reviews_scraping/spiders/ProductAnalysis.txt",
            "w")
        text_file.write(blogname)
        text_file.close()
        os.system(
            'scrapy runspider C:/Users/Rushil/Desktop/ncsu sem1/SE/New folder/SE_Project1/Amazon_Comments_Scrapper/amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_review.py -o reviews.json')
        final_comment = []
        with open('C:/Users/Rushil/Desktop/ncsu sem1/SE/New folder/SE_Project1/sentimental_analysis/reviews.json') as json_file:
            data = json.load(json_file)
            for p in range(1, len(data) - 1):
                a = data[p]['comment']
                final_comment.append(a)

        # final_comment is a list of strings!
        result = detailed_analysis(final_comment)
        return render(request, 'realworld/sentiment_graph.html', {"sentiment": result, "current_user": request.user})

    else:
        note = "Please Enter the product blog link for analysis"
        return render(request, 'realworld/productanalysis.html', {"note": note, "current_user": request.user})




def textanalysis(request):
    if request.method == 'POST':
        text_data = request.POST.get("Text", "")
        final_comment = text_data.split('.')

        # final_comment is a list of strings!
        result = detailed_analysis(final_comment)
        print("yolo",result)
        return render(request, 'realworld/sentiment_graph.html', {'sentiment': result, "current_user": request.user})
    else:
        note = "Enter the Text to be analysed!"
        return render(request, 'realworld/textanalysis.html', {'note': note, "current_user": request.user})


def get_video_comments(youtube, **kwargs):
    comments = []
    results = youtube.commentThreads().list(**kwargs).execute()

    while results:
        for item in results["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        # Check if there are more comments
        if "nextPageToken" in results:
            kwargs["pageToken"] = results["nextPageToken"]
            results = youtube.commentThreads().list(**kwargs).execute()
        else:
            break

    return comments

def get_video_captions(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        captions = [entry['text'] for entry in transcript]
        return captions
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@login_required(login_url="/login")    
def reddit_analysis(request):
    if request.method == 'POST':
        keyword = request.POST.get("keyword", "")
        reddit_read_only = praw.Reddit(client_id="Mb8Sp8_PcTtqHYn-5rRKsw", client_secret="w1oGqM9jiEMD__RQCMpE6LcLnwYqoQ", user_agent="Ok-Huckleberry-8806") 
        reddit_data = reddit_read_only.subreddit("all")
        to_be_analysed = []
        for post in reddit_data.search(keyword, limit=10):
            to_be_analysed.append(post.title)
        result = detailed_analysis(to_be_analysed)
        print(result)
        return render(request, 'realworld/sentiment_graph.html', {"sentiment": result, "current_user": request.user if request.user.is_authenticated else None})
    else:
        note = "Enter the reddit topic to be analyzed!"
        return render(request, 'realworld/redditdataanalysis.html', {'note': note, "current_user": request.user})
        
        

@login_required(login_url="/login")
def ytcaptions(request):
    if request.method == 'POST':
        print("called to ytcaptions")
        ytid = request.POST.get("ytid", "")
        # Replace with your API key or set up OAuth through GCP
        API_KEY = "AIzaSyB_NLPhehliexJvYFw5upWxtgTGDRNrlAw"
        VIDEO_ID = ytid  # Replace with the YouTube video ID

        youtube = build("youtube", "v3", developerKey=API_KEY)
        # Get captions for a specific video
        print(ytid)
        print(API_KEY)
        print(VIDEO_ID)
        try:
            captions = get_video_captions(VIDEO_ID)
            final_caption=[]
            if captions:
                  for i, caption in enumerate(captions, 1):
                        final_caption.append(caption)
            else:
                print("Failed to retrieve captions.")
    
            result = detailed_analysis(final_caption)

            return render(request, 'realworld/sentiment_graph.html', {"sentiment": result, "current_user": request.user if request.user.is_authenticated else None})
        except Exception as e:
            print(e)
            return render(request, 'realworld/error.html', {"current_user": request.user})
    else:
        note = "Enter the video ID to be analyzed!"
        return render(request, 'realworld/ytcaptions.html', {'note': note, "current_user": request.user})


@login_required(login_url="/login")
def ytanalysis(request):
    if request.method == 'POST':
        ytid = request.POST.get("ytid", "")
        # Replace with your API key or set up OAuth through GCP
        API_KEY = "AIzaSyAMkKPItHCg6LbG2WUu1aNX0SJQ57tdUFU"
        VIDEO_ID = ytid  # Replace with the YouTube video ID

        youtube = build("youtube", "v3", developerKey=API_KEY)
        # Get comments for a specific video
        try:
            comments = get_video_comments(
                youtube, part="snippet", videoId=VIDEO_ID, textFormat="plainText")
            print(comments)
            text_data = ''
            for i, comment in enumerate(comments, 1):
                text_data += f"{comment}"

            final_comment = text_data.split('.')

            # final_comment is a list of strings!
            result = detailed_analysis(final_comment)
            print(result)

            return render(request, 'realworld/sentiment_graph.html', {"sentiment": result, "current_user": request.user})
        except:
            return render(request, 'realworld/error.html', {"current_user": request.user})
    else:
        note = "Enter the video ID to be analysed!"
        return render(request, 'realworld/ytanalysis.html', {'note': note, "current_user": request.user})


@login_required(login_url="/login")
def audioanalysis(request):
    if request.method == 'POST':
        file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(file.name, file)
        pathname = "media/"
        extension_name = file.name
        extension_name = extension_name[len(extension_name)-3:]
        path = pathname+file.name
        result = {}
        print(path)
        text = speech_to_text(path)
        result = sentiment_analyzer_scores(text)
        print("Result")
        print(result)
        os.system(
            'cd /Users/sj941/Documents/GitHub/SE_Project1/sentimental_analysis/media/ && rm -rf *')
        return render(request, 'realworld/sentiment_graph.html', {'sentiment': result, "current_user": request.user})
    else:
        note = "Please Enter the audio file you want to analyze"
        return render(request, 'realworld/audio.html', {'note': note, "current_user": request.user})


def speech_to_text(filename):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print("TExt")
        print(text)
        return text


def sentiment_analyzer_scores(sentence):
    analyser = SentimentIntensityAnalyzer()
    print("Scores analysed")
    score = analyser.polarity_scores(sentence)
    return score
