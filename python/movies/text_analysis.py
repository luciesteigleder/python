import os
from textblob import TextBlob
from wordcloud import WordCloud
from collections import Counter
from django.conf import settings
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize





def generate_wordcloud(review_texts):
    # Generate word frequency dictionary
    word_freq = Counter()
    for text in review_texts:
        # words = text.split()
        word_freq += Counter(text)

    # Create wordcloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

    return wordcloud

def sentiment_analysis(documents):
    # Initialize counters
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    # Initialize a list to store all the review texts
    all_reviews = []

    for document in documents:
        # Perform sentiment analysis on review_text field
        review_text = document['reviewText']

        review_text_tokens = word_tokenize(review_text.lower())
        print("REVIEW TEXT")
        print(review_text)
        print(review_text_tokens)

        english_stopwords = stopwords.words('english')
        newStopWords = ['movie','film',"'", "'s", '(', ')', '.', "n't", ',', 'would']
        english_stopwords.extend(newStopWords)


        review_text_clean = [t for t in review_text_tokens if t not in english_stopwords]
        print("CLEAN TEXT")
        print(review_text_clean)
        # for sent in review_text_sentences:

        #     review_text_tokens = [word_tokenize(sent)]
        #     removing_custom_words = [words for words in review_text_tokens if not words in stpwrd]
        #     print("COMPARISON")
        #     print(review_text)
        #     print(removing_custom_words)

        def getSubjectivity(text):
            return TextBlob(text).sentiment.subjectivity

        def getPolarity(text):
            return TextBlob(text).sentiment.polarity

        subjectivity = getSubjectivity(review_text)
        polarity = getPolarity(review_text)

        # Perform analysis
        if polarity < -0.63:
            analysis = 'Negative'
            negative_count += 1
        elif polarity > 0.36:
            analysis = 'Positive'
            positive_count += 1
        else:
            analysis = 'Neutral'
            neutral_count += 1

        # Add review text to the list
        all_reviews.append(review_text_clean)

        # Print the results in the console
        # print("Subjectivity:", subjectivity)
        # print("Polarity:", polarity)
        # print("Analysis:", analysis)
        # print("--------------------")
    # print('ALL REVIEWS')
    # print(all_reviews)
    # Generate the word cloud


    wordcloud = generate_wordcloud(all_reviews)

    # Create the directory if it doesn't exist
    wordcloud_directory = os.path.join(settings.MEDIA_ROOT, 'images')
    os.makedirs(wordcloud_directory, exist_ok=True)

    # Save the word cloud as an image file
    wordcloud_path = os.path.join(wordcloud_directory, 'wordcloud.png')
    wordcloud.to_file(wordcloud_path)

    # Get the relative path to the media directory
    relative_wordcloud_path = os.path.join(settings.MEDIA_URL, 'images', 'wordcloud.png')

    # Return the sentiment analysis results and the path to the word cloud image
    return {
        'positive_count': positive_count,
        'negative_count': negative_count,
        'neutral_count': neutral_count,
        'wordcloud_path': relative_wordcloud_path
    }