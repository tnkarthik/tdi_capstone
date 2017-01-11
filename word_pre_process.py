import re
from nltk.corpus import stopwords
def clean_text(text_list):
    clean_text_list = []
    for text in text_list:
        text = re.sub("[^A-Z,a-z]"," ",text)
        #print text
        words = re.split(",|;| |\s+",text)
        stop_words = set(stopwords.words("english"))
        clean_text_list = clean_text_list + [' '.join([word for word in words if word and  not (word in stop_words)])]
    return clean_text_list
    #print words
    
from sklearn.feature_extraction.text import CountVectorizer
def words_to_ngram(words,ngram_min=1,ngram_max=1):
    vectorizer = CountVectorizer(analyzer = "word",\
                                tokenizer = None,\
                                preprocessor = None,\
                                stop_words = None,\
                                max_features = 5000,
                                ngram_range = (ngram_min, ngram_max))
    features = vectorizer.fit_transform(words)
    feature_names = vectorizer.get_feature_names()
    return (features,feature_names)

