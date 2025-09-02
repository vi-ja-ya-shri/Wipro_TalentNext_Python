# 1. Check if string has only octal digits
import re

strings = ['789', '123', '004']
pattern = re.compile(r'^[0-7]+$')

for s in strings:
    if pattern.match(s):
        print(f"{s} is octal")
    else:
        print(f"{s} is not octal")


# 2. Extract user id, domain name, and suffix from emails
import re

emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = re.compile(r'(\w+)@([A-Za-z]+)\.(\w+)')
matches = pattern.findall(emails)

for match in matches:
    print(match)


# 3. Split irregular sentence into proper words
import re

sentence = """A, very    very; irregular_sentence"""
words = re.split(r'[;,_\s]+', sentence)
cleaned = " ".join(words)
print(cleaned)


# 4. Clean up tweet (remove URLs, hashtags, mentions, punctuations, RTs, CCs)
import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

tweet = re.sub(r'RT\s+@\w+:', '', tweet)   
tweet = re.sub(r'cc:\s*@\w+', '', tweet)   
tweet = re.sub(r'@\w+', '', tweet)         
tweet = re.sub(r'#\w+', '', tweet)         
tweet = re.sub(r'http\S+', '', tweet)    
tweet = re.sub(r'[^\w\s]', '', tweet)     

cleaned_tweet = " ".join(tweet.split())    
print(cleaned_tweet)

# 5. Extract all text between HTML tags
import re
import requests


r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text


pattern = re.compile(r'>([^<]+)<')
matches = pattern.findall(html)


cleaned = [m.strip() for m in matches if m.strip()]
print(cleaned)

# 6. Identify words that begin and end with the same character
import re

words = ["civic", "trust", "widows", "maximum", "museums", "aa", "as"]

pattern = re.compile(r'^(.).*\1$')   # first char = last char
result = [w for w in words if pattern.match(w)]

print(result)