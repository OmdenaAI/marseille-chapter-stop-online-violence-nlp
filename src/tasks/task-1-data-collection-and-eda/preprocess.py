import difflib
import itertools
import re
import warnings
#pip install emoji
#nltk.download('stopwords')
import emoji
import nltk
from nltk.stem.snowball import FrenchStemmer
import string



# English and french punctuations
PUNCTUATIONS = '''!()-[]{};:'"\\,<>./?@#$€£₭฿¥%^&*_~'''

#list of french stop words
STOPWORDS =  nltk.corpus.stopwords.words("french")
print(STOPWORDS)


# you can choose to keep basic emoticons in your text if you think it will help in your classification training
emoji_pattern = re.compile("["
                           #  u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f932"
                           u"\u200f"
                           u"\U0001F914"
                           u"\U0001F923"
                           u"\u200D"
                           u"\u202c"
                           u"\u2069"
                           u"\u2066"
                           u"\U0001F926"
                           u"\U0001F917"
                           u"\U0001f928"
                           u"\t"
                           u"\u200e"
                           "]+", flags=re.UNICODE)



def remove_urls(text):
    # Remove any string that starts with either http:// , https:// , ftp:// or www. plus
    # any combination of non white space characters.
    text = re.sub('http[s]?://\S+', '', text, flags=re.MULTILINE)
    text = re.sub('ftp?://\S+', '', text, flags=re.MULTILINE)
    text = re.sub('www.\S+', '', text, flags=re.MULTILINE)
    return text

def remove_accents(text):

    #Removes accents from a given string.

    text = re.sub('[éèêë]', "e", text)
    text = re.sub("[ùûü]", "u", text)
    text = re.sub("[ôö]", "o", text)
    text = re.sub("ç", "c", text)
    text = re.sub("[ïî]", "i", text)
    text = re.sub("[àâ]", "a", text)
    text = re.sub("ÿ", "y", text)
    return text

#from a string from a list of tokens
def join_tokens(tokens=[], sep=" "):
    return sep.join(tokens)

#remove emojis from a string
def remove_emoji(text):
    return emoji_pattern.sub(r' ', text)

#remove punctuations from the string
def remove_punctuations(text):
    translator = str.maketrans('', '', PUNCTUATIONS)
    return text.translate(translator)



def join_tokens(tokens, sep=" "):
     return sep.join(tokens)

def remove_stopwords_from_tokens(tokens):

    return join_tokens([i for i in tokens if i.lower() not in STOPWORDS],' ')
# if a token is a number it is removed from the list of tokens
def remove_digits(text):
    text = join_tokens([w for w in text.split(" ") if not w.isdigit()])
    return text

# remove any digit in the text
def remove_all_numbers(text):
    return re.sub(r'\d+', ' ', text)


def remove_extra_whitespaces(text):
    return ' '.join(text.split())

#functions can be added or removed
def preproc(data=""):
    data = str(data)
    text = remove_urls(data)  # ok
    text = remove_punctuations(text)
    #text = remove_accents(text)
    text= remove_stopwords_from_tokens(text.split())
    text = remove_emoji(text)
    text = remove_digits(text)
    text = remove_extra_whitespaces(text)
    return text

def stem(tokens):

    stemmer = FrenchStemmer()

    for item in tokens:
        stems.append(stemmer.stem(item))

    return stems

print(remove_stopwords_from_tokens("je suis contente. A  savoir si j'ai dejà  fait ce travail 😄 ".split()))