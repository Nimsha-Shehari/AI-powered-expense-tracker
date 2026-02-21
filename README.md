#AI-Powered Expense Tracker

An intelligent mobile expense tracking system that automates receipt processing using Optical Character Recognition (OCR) and Machine Learning for expense categorization.

📌 Overview

Traditional expense trackers require manual input, which is time-consuming and error-prone. This project introduces an AI-driven solution that allows users to scan bills and automatically generate categorized expense records.

The system follows a three-stage pipeline:

Bill Scanning – Capture receipt images via mobile application

Text Extraction – Extract bill details using Tesseract OCR

Expense Classification – Categorize expenses using ML models

⚙️ Features

Receipt image scanning

Automated text extraction (OCR)

AI-based expense categorization

Duplicate receipt handling concept

Multi-category expense classification

Performance evaluation and visualization

🧠 Machine Learning Pipeline

Dataset: 17,141 labeled expense records

Text preprocessing and cleaning

TF-IDF vectorization

Class imbalance handling using SMOTE

Classification using:

Support Vector Machine (SVM)

Neural Network (TensorFlow/Keras Sequential Model)

📊 Model Performance

Overall Accuracy: 92%

Evaluation Metrics:

Precision

Recall

F1 Score

Confusion Matrix

ROC Curve Analysis

🛠️ Tech Stack

Python

Scikit-learn

TensorFlow / Keras

Tesseract OCR

Pandas & NumPy

Flutter (Mobile Frontend)

🚀 Future Improvements

Multilingual receipt support (Sri Lankan context)

Duplicate receipt detection

AI-powered spending insights

SMS-based expense logging

Expanded regional datasets

👩‍💻 Authors

Developed as part of an Artificial Intelligence research project at Wayamba University of Sri Lanka.
