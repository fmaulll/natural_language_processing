# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.model_selection import train_test_split

# # Load and preprocess your dataset# Sample text data (public reports)
# text_data = [
#     "There is a fire in the forest near the village. Urgent action needed!",
#     "The internet connection is slow in our area. Please fix it.",
#     "The road in front of our house is in very bad condition and needs repair.",
#     "We need more medical facilities in our community.",
#     "The school building is in poor condition. It requires maintenance.",
#     "Our neighborhood needs a park for children to play.",
#     "There's a water shortage in our town. We need water supply improvements.",
#     "The public library is overcrowded and needs expansion.",
#     "Our streets need better street lighting for safety at night.",
#     "There are potholes on the highway causing accidents. Road maintenance is required.",
#     # ... more reports ...
# ]

# # Sample ministry labels corresponding to each report
# ministry_labels = [
#     "Ministry of Environment",
#     "Ministry of Communication and Information Technology",
#     "Ministry of Public Works",
#     "Ministry of Health",
#     "Ministry of Education",
#     "Ministry of Parks and Recreation",
#     "Ministry of Water Resources",
#     "Ministry of Culture and Arts",
#     "Ministry of Public Safety",
#     "Ministry of Transportation",
#     # ... more labels ...
# ]

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(text_data, ministry_labels, test_size=0.2, random_state=42)

# # Vectorize the text data using TF-IDF
# vectorizer = TfidfVectorizer()
# X_train_tfidf = vectorizer.fit_transform(X_train)
# X_test_tfidf = vectorizer.transform(X_test)

# # Train a text classification model
# classifier = MultinomialNB()
# classifier.fit(X_train_tfidf, y_train)

# # Predict ministry agencies for test data
# predictions = classifier.predict(X_test_tfidf)

# # Evaluate the model and use it to route reports
# print(X_test)
# print(predictions)
import re

# Sample public reports
reports = [
    "There is a fire in the forest near the village. Urgent action needed!",
    "The internet connection is slow in our area. Please fix it.",
    "Our neighborhood needs a park for children to play.",
    "There's a water shortage in our town. We need water supply improvements.",
    "The public library is overcrowded and needs expansion.",
    "Our streets need better street lighting for safety at night.",
    "There are potholes on the highway causing accidents. Road maintenance is required.",
    "Critical water shortage in our town demands immediate attention. Ministry of Environment, we need assistance",
]

# Define ministry agencies and their associated keywords
ministries = {
    "Ministry of Environment": ["fire", "forest", "urgent action", "water"],
    "Ministry of Communication and Information Technology": ["internet", "connection", "slow"],
    "Ministry of Parks and Recreation": ["park", "children", "play"],
    "Ministry of Water Resources": ["water shortage", "water supply"],
    "Ministry of Culture and Arts": ["public library", "overcrowded", "expansion"],
    "Ministry of Public Safety": ["street lighting", "safety", "night"],
    "Ministry of Transportation": ["potholes", "highway", "road maintenance"],
}

# Function to filter reports to ministries based on keywords
def filter_reports(reports, ministries):
    filtered_reports = {ministry: [] for ministry in ministries}

    for report in reports:
        report = report.lower()  # Convert report to lowercase for case-insensitive matching

        for ministry, keywords in ministries.items():
            for keyword in keywords:
                if re.search(rf"\b{re.escape(keyword)}\b", report):
                    filtered_reports[ministry].append(report)
                    break

    return filtered_reports

# Filter the reports
filtered_reports = filter_reports(reports, ministries)

# Print the filtered reports for each ministry
for ministry, reports in filtered_reports.items():
    print(f"{ministry}:")
    for report in reports:
        print(report)
    print()