from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Sample text data for ministries
ministries_data = {
    "Kementrian Komunikasi": ["Report 1 about communication issues.", "Another report about internet problems."],
    "Kementrian PUPR": ["Road repair request near my house.", "Report on public works project."],
    "Kementrian Kesehatan": ["Medical facilities report.", "Healthcare service issues."],
    # Add more ministries and their corresponding data
}

# Combine all reports into one dataset
all_reports = []
all_ministries = []

for ministry, reports in ministries_data.items():
    all_reports.extend(reports)
    all_ministries.extend([ministry] * len(reports))

    print(all_reports)
    print()
    print(all_ministries)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(all_reports, all_ministries, test_size=0.2, random_state=42)

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a separate text classification model for each ministry
ministry_classifiers = {}

for ministry in ministries_data.keys():
    classifier = MultinomialNB()
    mask = [label == ministry for label in y_train]
    classifier.fit(X_train_tfidf[mask], [ministry] * sum(mask))
    ministry_classifiers[ministry] = classifier

# Sample new report
new_report = "Road repair request near my house."

# Vectorize the new report
new_report_tfidf = vectorizer.transform([new_report])

# Predict the ministry for the new report using the corresponding model
predicted_ministries = {}

for ministry, classifier in ministry_classifiers.items():
    predicted_ministry = classifier.predict(new_report_tfidf)
    predicted_ministries[ministry] = predicted_ministry[0]

print("Report Text:", new_report)
print("Predicted Ministries:", predicted_ministries)