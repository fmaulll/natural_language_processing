from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

app = Flask(__name__)

# Download NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Tokenization and remove punctuation
    tokens = [word.strip(string.punctuation) for word in text.split()]

    # Remove stopwords
    stop_words = set(stopwords.words('indonesian'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Reassemble the text
    processed_text = ' '.join(tokens)

    return processed_text

def load_data_from_json(data_file):
    with open(data_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def train_svm_classifier(data):
    # Split the data into features (X) and labels (y)
    X = [preprocess_text(entry['text']) for entry in data]
    y = [entry['label'] for entry in data]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a pipeline with TfidfVectorizer and Support Vector Machine (SVC)
    model = make_pipeline(TfidfVectorizer(), SVC())

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = model.predict(X_test)

    # Evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"SVM Classifier Accuracy: {accuracy:.2f}")

    # Print classification report (includes precision, recall, and F1-score)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    return model

def predicted_category(report):
    data_file = 'data.json'
    data = load_data_from_json(data_file)
    
    svm_model = train_svm_classifier(data)

    # Preprocess the input text before making predictions
    processed_report = preprocess_text(report)

    # Make a prediction using the trained model
    predicted_category = svm_model.predict([processed_report])[0]

    return {"predicted_category": predicted_category}

