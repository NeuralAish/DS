import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Input text
text = "Data Science is an amazing field of study"

# Tokenization
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered = [word for word in tokens if word.lower() not in stop_words]

# Output
print("Tokens:", tokens)
print("Filtered:", filtered)
