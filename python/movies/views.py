from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.conf import settings
from pymongo import MongoClient
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from .text_analysis import sentiment_analysis

plt.rcParams.update({'font.size': 32})

class HomepageView(View):
    @csrf_exempt
    def get(self, request):
        return render(request, 'movies/homepage.html')

    @csrf_exempt
    def post(self, request):
        movie_name = request.POST.get('movie_name')
        if movie_name:
            request.session['movie_name'] = movie_name
            return redirect('results')
        return render(request, 'movies/homepage.html')

class ResultsView(View):
    @csrf_exempt
    def get(self, request):
        movie_name = request.session.get('movie_name')
        if movie_name:
            # Connect to MongoDB Atlas
            client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
            db = client[settings.DATABASES['default']['NAME']]
            collection = db.reviews

            # Retrieve the information from the database
            documents = collection.find()
            # for document in documents:
                # print("DOCUMENT ONE BY ONE")
                # print(document)

            # SENTIMENT ANALYSIS
            # Perform sentiment analysis
            analysis_results = sentiment_analysis(documents)

            # Get the sentiment analysis results
            positive_count = analysis_results['positive_count']
            negative_count = analysis_results['negative_count']
            neutral_count = analysis_results['neutral_count']

            # Calculate the percentages
            total_reviews = positive_count + negative_count + neutral_count
            positive_text_percentage = round((positive_count / total_reviews) * 100)
            neutral_text_percentage = round((neutral_count / total_reviews) * 100)
            negative_text_percentage = round((negative_count / total_reviews) * 100)

            # Generate the wordcloud
            wordcloud_path = analysis_results['wordcloud_path']

            # REVIEW SCORE
            review_scores = [doc['reviewScore'] for doc in collection.find() if doc['reviewScore'] is not None]
            # Count the number of review scores in each category
            positive_count = len([score for score in review_scores if score >= 7])
            neutral_count = len([score for score in review_scores if 4 <= score <= 6])
            negative_count = len([score for score in review_scores if score <= 3])

            # Calculate the percentages based on review scores
            total_reviews = len(review_scores)
            positive_score_percentage = round((positive_count / total_reviews) * 100)
            neutral_score_percentage = round((neutral_count / total_reviews) * 100)
            negative_score_percentage = round((negative_count / total_reviews) * 100)

            # Generate the chart
            chart_path = self.generate_chart(review_scores)

            return render(request, 'movies/results.html', {
                'wordcloud_path': wordcloud_path,
                'positive_score_percentage': positive_score_percentage,
                'neutral_score_percentage': neutral_score_percentage,
                'negative_score_percentage': negative_score_percentage,
                'positive_text_percentage': positive_text_percentage,
                'neutral_text_percentage': neutral_text_percentage,
                'negative_text_percentage': negative_text_percentage,
                'movie_name': movie_name,
                'chart_path': chart_path
            })
        else:
            return redirect('homepage')

    def generate_chart(self, review_scores):

        # Clear any existing plots
        plt.clf()

        # Your data for the chart
        x = range(1, 11)
        y = [review_scores.count(score) for score in x]

        # Create the bar chart
        plt.bar(x, y)
        plt.xticks(range(1, 11))

        # Get the current axis object
        # ax = plt.gca()

        # Set the font family for the tick labels
        # ax.set_xticklabels(ax.get_xticks(), fontfamily='Helvetica')
        # ax.set_yticklabels(ax.get_yticks(), fontfamily='Roboto')

        # Create the directory if it doesn't exist
        chart_directory = os.path.join(settings.MEDIA_ROOT, 'images')
        os.makedirs(chart_directory, exist_ok=True)

        # Save the chart as an image file
        chart_path = os.path.join(chart_directory, 'chart.png')
        plt.savefig(chart_path, transparent=True)

        # Get the relative path to the media directory
        relative_chart_path = os.path.join(settings.MEDIA_URL, 'images', 'chart.png')

        return relative_chart_path