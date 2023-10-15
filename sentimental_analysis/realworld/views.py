from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from django.template.defaulttags import register
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from .utilityFunctions import *
import os
import json
import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from .signup import SignUpForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


def update_user_data(user):
    Profile.objects.update_or_create(user=user,)


def signin(request):
    return render(request, 'realworld/signin.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return render(request, 'realworld/signin.html')
    else:
        form = SignUpForm()
    return render(request, 'realworld/signup.html', {'form': form})


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
        print(item)
        cleantext = get_clean_text(str(item))
        print(cleantext)
        sentiment = sentiment_scores(cleantext)
        print(sentiment)
        compound_score = sentiment['compound']

        pos_count += sentiment['pos']
        neu_count += sentiment['neu']
        neg_count += sentiment['neg']

    total = pos_count + neu_count + neg_count
    result_dict['pos'] = (pos_count/total)
    result_dict['neu'] = (neu_count/total)
    result_dict['neg'] = (neg_count/total)

    return result_dict


def input(request):
    if request.method == 'POST':
        file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(file.name, file)
        pathname = "media/"
        extension_name = file.name
        extension_name = extension_name[len(extension_name)-3:]
        path = pathname+file.name
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
        # Sentiment Analysis
        os.system(
            'cd /Users/sj941/Documents/GitHub/SE_Project1/sentimental_analysis/media/ && rm -rf *')
        return render(request, 'realworld/sentiment_graph.html', {'sentiment': result})
    else:
        note = "Please Enter the Document you want to analyze"
        return render(request, 'realworld/home.html', {'note': note})


def productanalysis(request):
    if request.method == 'POST':
        blogname = request.POST.get("blogname", "")
        text_file = open(
            "D:/NCSU/Sem 1/Software Engineering/SE_Project1/Amazon_Comments_Scrapper/amazon_reviews_scraping/amazon_reviews_scraping/spiders/ProductAnalysis.txt",
            "w")
        text_file.write(blogname)
        text_file.close()
        os.system(
            'scrapy runspider D:/NCSU/Sem 1/Software Engineering/SE_Project1/Amazon_Comments_Scrapper/amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_review.py -o reviews.json')
        final_comment = []
        with open('D:/NCSU/Sem 1/Software Engineering/SE_Project1/sentimental_analysis/reviews.json') as json_file:
            data = json.load(json_file)
            for p in range(1, len(data) - 1):
                a = data[p]['comment']
                final_comment.append(a)

        # final_comment is a list of strings!
        result = detailed_analysis(final_comment)
        print(result)
        return render(request, 'realworld/sentiment_graph.html', {'sentiment': result})

    else:
        note = "Please Enter the product blog link for analysis"
        return render(request, 'realworld/productanalysis.html', {'note': note})

# Custom template filter to retrieve a dictionary value by key.


def textanalysis(request):
    if request.method == 'POST':
        text_data = request.POST.get("Text", "")
        final_comment = text_data.split('.')

        # final_comment is a list of strings!
        result = detailed_analysis(final_comment)
        print(result)
        return render(request, 'realworld/sentiment_graph.html', {'sentiment': result})
    else:
        note = "Enter the Text to be analysed!"
        return render(request, 'realworld/textanalysis.html', {'note': note})


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
        # Sentiment Analysis
        os.system(
            'cd /Users/sj941/Documents/GitHub/SE_Project1/sentimental_analysis/media/ && rm -rf *')
        return render(request, 'realworld/sentiment_graph.html', {'sentiment': result})
    else:
        note = "Please Enter the audio file you want to analyze"
        return render(request, 'realworld/audio.html', {'note': note})


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
    # print("{:-<40} {}".format(sentence, str(score)))
    return score


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


def ytanalysis(request):
    if request.method == 'POST':
        ytid = request.POST.get("ytid", "")
        print(ytid)
        # Replace with your API key or set up OAuth through GCP
        API_KEY = "AIzaSyAMkKPItHCg6LbG2WUu1aNX0SJQ57tdUFU"
        VIDEO_ID = ytid  # Replace with the YouTube video ID

        youtube = build("youtube", "v3", developerKey=API_KEY)
        # Get comments for a specific video
        comments = get_video_comments(
            youtube, part="snippet", videoId=VIDEO_ID, textFormat="plainText")

        text_data = ''
        for i, comment in enumerate(comments, 1):
            text_data += f"{comment}"

        final_comment = text_data.split('.')

        # final_comment is a list of strings!
        result = detailed_analysis(final_comment)
        print(result)
        return render(request, 'realworld/sentiment_graph.html', {'sentiment': result})

    else:
        note = "Enter the video ID to be analysed!"
        return render(request, 'realworld/ytanalysis.html', {'note': note})


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key, 0)
