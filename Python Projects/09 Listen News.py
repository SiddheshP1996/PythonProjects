""""""
"""
Akhbaar Padhke Sunaao
for newsapi.org
https://newsapi.org/ 

install pywin32 using pip install pywin32

take top 10 relevant news from newsapi and after running the program give today's fresh news.

"""

import requests
import json


def speak(sentence):
    from win32com.client import Dispatch
    bol = Dispatch("SAPI.SpVoice")
    bol.Speak(sentence)


if __name__ == '__main__':
    speak("News For Today.. Let's Begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY"
    news = requests.get(url).text
    print(news)
    # print(news["status"])  # will throw an error TypeError: string indices must be integers, not 'str'
    news_dict = json.loads(news)  # converted to a python object using json module
    # print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])
        speak(article['title'])
        speak("Moving on to the next news .. Listen Carefully !!")
    speak("Thanks for Listening ...")
