# Analyser of Movie Reviews - Flask
The craze for watching movies will never decrease and during the current situation, the increase of people watching movies on internet platforms is burgeoning. It is necessary for Multinational Companies to invest in the best movies and make them available to the proper target audience. Using the Flask app which is proposed, this can be achieved and will be helpful to find the target audience and companies to invest on propitious movies. In this app, people login or create an account and provide reviews about the movie. These reviews are stored in MONGODB database and Sentiment Analysis and scores are provided respectively. Finally, one can check the review of the movie, where it displays the average audience score with their gender information and reach of the movie in different states of the country

## Description
The application takes user input in the form of movie reviews and uses machine learning models to analyse the sentiment of the reviews. The application includes a pre-trained machine learning model for sentiment analysis, which predicts whether a given review is positive or negative.

The application is built using Flask, a lightweight web framework for Python. The application includes a user interface that allows users to enter movie reviews and receive sentiment analysis results in real time.

## Installation
To run the application, you will need to have Python 3 installed on your local machine. You can download Python from the official website: https://www.python.org/downloads/

Once Python is installed, you can download the repository from this GitHub page and install the required dependencies using the following command:

## Copy code
pip install -r requirements.txt
This will install all the required Python libraries for the application.

## Usage
To use the application, navigate to the project directory in your terminal and run the following command:

## Copy code
python app.py
This will start the Flask application and make it available at http://localhost:5000. You can access the user interface by opening a web browser and navigating to this address.

To use the application, enter a movie review in the text box provided and click the "Analyse" button. The application will return a sentiment analysis result, indicating whether the review is positive or negative.

You can also modify the machine learning model or the user interface to suit your needs. The application includes detailed comments and explanations in the code.

## Data
The machine learning model used in this application is trained on the IMDB movie review dataset, which includes over 50,000 movie reviews with positive and negative sentiment labels.

## Contributing
This repository is open for contributions. If you find any issues or have any suggestions, feel free to create a pull request or open an issue.






