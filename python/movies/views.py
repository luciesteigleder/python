from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.conf import settings
from pymongo import MongoClient
import os
import matplotlib.pyplot as plt

class HomepageView(View):
    @csrf_exempt
    def get(self, request):
        return render(request, 'movies/homepage.html')

    @csrf_exempt
    def post(self, request):
        name = request.POST.get('movie_name')
        if name:
            print(name)
            return redirect('results')
        return render(request, 'movies/homepage.html')


class ResultsView(View):
    def get(self, request):
        # Connect to MongoDB Atlas
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        collection = db.reviews

        # Retrieve the information from the database
        review_scores = [doc['reviewScore'] for doc in collection.find()]

        # Generate the chart
        chart_path = self.generate_chart(review_scores)

        return render(request, 'movies/results.html', {'chart_path': chart_path})
    
    def post(self, request):

        # Connect to MongoDB Atlas
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        collection = db.reviews

        # Clear any existing plots
        plt.clf()
        
        # Retrieve the information from the database
        review_scores = [doc['reviewScore'] for doc in collection.find()]

        # Generate the chart
        chart_path = self.generate_chart(review_scores)

        return render(request, 'movies/results.html', {'chart_path': chart_path})


    def generate_chart(self, review_scores):

         # Clear any existing plots
        plt.clf()

        # Your data for the chart
        x = range(1, 11)
        y = [review_scores.count(score) for score in x]

        # Create the bar chart
        plt.bar(x, y)
        plt.xticks(range(1, 11))

        # Create the directory if it doesn't exist
        chart_directory = os.path.join(settings.MEDIA_ROOT, 'images')
        os.makedirs(chart_directory, exist_ok=True)

        # Save the chart as an image file
        chart_path = os.path.join(chart_directory, 'chart.png')
        plt.savefig(chart_path)

        # Get the relative path to the media directory
        relative_chart_path = os.path.join(settings.MEDIA_URL, 'images', 'chart.png')

        return relative_chart_path