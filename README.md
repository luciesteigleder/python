# Welcome to Senti-movie!

This basic application pulls data on **movie reviews** from the imdb website, and analyses them!
This project was developed as an educational project. The objectives was two-fold:

- Take a first dive into programmation with python and Django.
- Explore Natural Language Processing.

# How does it work?

## First step: Scraping

When the user enters the name of a movie, the Express app will connect to the imdb API and get the first page of reviews, ordered by date (most recent). The review text and review score are saved in a MongoDB collection.

## Second step: Analysis

The platform then goes to a second page with the results. The two fields will be analysed:

- The review score: a distribution of the different rates, and a percentage of positive (>7), neutral (4<>6) and negative (<3) scores.
- The analysis of the comments: A sentiment analysis is made on the review texts, and also display a percentage of positive, negative and neutral comments. Additionally, a word cloud is presented to showcase the words that have been the most used by the reviewers.

# How to run this project

## Launch the servers

Unfortunately, Senti-Movie isn't hosted on an online server (yet!). So it has to be run locally.
Two servers have to be launched: Django for the platform, and Express for the scraping.

## Use the app

Just type the name of the movie of your choice in the text field!

# Self-reflection and future improvements

## Quick fixes

1. The first step would be to host the app on heroku
2. I would like to scrap more data: not just only the first page but maybe all the comments?
3. Change the design! At the moment, it is quite dull. But frontend wasn't definitively the priority for this project.
4. add the classical protections (against XSS, etc)
5. Fix all the current issues on the Django server

## More ambitious

6. The sentiment analysis can definitively be improved. At the moment, the score and reviews percentages don't match. The polarity score is potentially not distributed uniformally. (1/3 - 1/3 - 1/3) like it can be the case for the ratings. And a more careful pre-proessing has to be done with the text (remove punctuation,, remove the name of the movie itself from the wordcloud etc). But this would require a deeper understanding of how NLP work, and an ability to develop my own models for analysis. Hopefully in the future!
7. Improve the search on imdb. At the moment, the text typed by the user is simply put in the search bar, and the app scrapes the data from the first link that appears, but with typos, sequels or unknown movies, it might not work.
