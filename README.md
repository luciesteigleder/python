# Welcome to Senti-movie!

This basic application pulls data on **movie reviews** from the IMDb website and analyzes them! This project was developed as an educational project with two objectives:

- Take a first dive into programming with Python and Django.
- Explore Natural Language Processing.

# How does it work?

## First step: Scraping

When the user enters the name of a movie, the Express app connects to the IMDb API and retrieves the first page of reviews, ordered by date (most recent). The review text and review score are then saved in a MongoDB collection.

## Second step: Analysis

The platform then displays the results on a second page. The following fields are analyzed:

- The review score: It shows the distribution of different ratings and the percentage of positive (>7), neutral (4-6), and negative (<3) scores.
- The analysis of the comments: A sentiment analysis is performed on the review texts. It also displays the percentage of positive, negative, and neutral comments. Additionally, a word cloud is presented to showcase the most commonly used words by the reviewers.

# How to run this project

## Launch the servers

Unfortunately, Senti-Movie is not currently hosted on an online server. Therefore, it needs to be run locally. You need to launch two servers: Django for the platform and Express for the scraping.

## Using the app

Simply type the name of the movie of your choice in the text field!

# Self-reflection and future improvements

## Quick fixes

1. The first step would be to host the app on Heroku.
2. I would like to scrape more data, not just the first page but maybe all the comments.
3. Change the design! Currently, it is quite dull, but frontend was not the primary focus for this project.
4. Add the necessary protections against XSS and other vulnerabilities.
5. Fix all the current issues on the Django server.

## More ambitious improvements

6. The sentiment analysis can definitely be improved. Currently, the score and review percentages don't match, and the polarity score may not be distributed uniformly (1/3 - 1/3 - 1/3) as it can be the case for ratings. A more careful preprocessing of the text is required, such as removing punctuation and the movie's name from the word cloud. However, achieving this would require a deeper understanding of how NLP works and the ability to develop custom analysis models. Hopefully, this can be explored in the future!
7. Improve the search functionality on IMDb. Currently, the text typed by the user is simply put in the search bar, and the app scrapes data from the first link that appears. However, this approach may not work well with typos, sequels, or unknown movies.
