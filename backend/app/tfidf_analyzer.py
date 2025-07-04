# Converts text to lowercase, removes special characters/numbers, and normalizes whitespace.
# Tokenizes the text and removes stopwords using NLTK for cleaner TF-IDF results.
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data (quietly to avoid repeated downloads)
try:
    nltk.download('punkt_tab', quiet=True)
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
except Exception as e:
    print(f"Error downloading NLTK resources: {e}")

# Preprocess text (cleaning, tokenizing, removing stopwords)
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters, numbers, and extra whitespace
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\b\d{4}\b', '', text)  # Remove years like 20xx
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'\bxx\b', '', text)     # Remove 'xx'
    text = re.sub(r'[•➢]', '', text)  # Remove common bullet point symbols
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Join tokens back into a string
    return ' '.join(tokens)

# TF-IDF analysis to extract key terms from resume
def analyze_resume_with_tfidf(resume_text):
    try:
        # Preprocess the resume text
        processed_text = preprocess_text(resume_text)
        if not processed_text.strip():
            return {"error": "No valid text extracted for TF-IDF analysis"}

        # Initialize TF-IDF vectorizer
        vectorizer = TfidfVectorizer(max_features=50, ngram_range=(1, 2))  # Include unigrams and bigrams
        tfidf_matrix = vectorizer.fit_transform([processed_text])

        # Get feature names and their TF-IDF scores
        feature_names = vectorizer.get_feature_names_out()
        tfidf_scores = tfidf_matrix.toarray()[0]
        keyword_scores = {feature_names[i]: tfidf_scores[i] for i in range(len(feature_names))}

        # Sort keywords by score and return top 10
        top_keywords = sorted(keyword_scores.items(), key=lambda x: x[1], reverse=True)[:10]
        return {
            "top_keywords": [{"term": term, "score": round(score, 4)} for term, score in top_keywords]
        }
    except Exception as e:
        return {"error": f"TF-IDF analysis failed: {str(e)}"}