from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import re
import nltk
import string

def predicted_category(report):
    with open('data.json', 'r') as data:
        cl = NaiveBayesClassifier(data, format="json")

    text_report = report

    blob = TextBlob(text_report, classifier=cl)

    prob_dist = cl.prob_classify(text_report)
    prob_dist.max()

    print(blob.classify())

    print()
    print("Probability:")
    print(f"Dinas Sumberdaya Air dan Bina Marga Kota Bandung: {round(prob_dist.prob('Dinas Sumberdaya Air dan Bina Marga Kota Bandung'), 2)}")
    print(f"Satuan Polisi Pamong Praja Kota Bandung: {round(prob_dist.prob('Satuan Polisi Pamong Praja Kota Bandung'), 2)}")
    print(f"Dinas Perhubungan Kota: {round(prob_dist.prob('Dinas Perhubungan Kota'), 2)}")
    print(f"Dinas Kependudukan dan Pencatatan Sipil Kota Bandung: {round(prob_dist.prob('Dinas Kependudukan dan Pencatatan Sipil Kota Bandung'), 2)}")

    return {
        "predicted_authorities": blob.classify(),
        "Dinas Sumberdaya Air dan Bina Marga Kota Bandung": round(prob_dist.prob('Dinas Sumberdaya Air dan Bina Marga Kota Bandung'), 2),
        "Satuan Polisi Pamong Praja Kota Bandung": round(prob_dist.prob('Satuan Polisi Pamong Praja Kota Bandung'), 2),
        "Dinas Perhubungan Kota": round(prob_dist.prob('Dinas Perhubungan Kota'), 2),
        "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung": round(prob_dist.prob('Dinas Kependudukan dan Pencatatan Sipil Kota Bandung'), 2)
    }
