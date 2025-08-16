import nltk
from nltk.stem import WordNetLemmatizer
import difflib
import re

nltk.download("wordnet", quiet=True)

lemmatizer = WordNetLemmatizer()

chat_pairs = {
    "what is python": "Python is a popular programming language.",
    "who created python": "Guido van Rossum created Python in 1991.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI.",
    "tell me something interesting": "Did you know? Python is named after 'Monty Python', not the snake!",
    "how are you": "I'm doing great, thanks for asking! 😊",
    "what can you do": "I can answer questions about Python, AI, and more. Ask away!",
    "bye": "Goodbye! Have a nice day 💖",
    "exit": "Goodbye! Stay safe and happy 🌸"
}

def custom_tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())

def preprocess(text):
    tokens = custom_tokenize(text)
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(lemmatized)

def get_best_match(processed_input, possibilities):
    matches = difflib.get_close_matches(processed_input, possibilities, n=1, cutoff=0.5)
    return matches[0] if matches else None

def chatbot():
    print("\n🤖 Welcome to NLP Chatbot!")
    print("You can ask me things like:")
    print("• What is Python?")
    print("• Who created Python?")
    print("• What is AI?")
    print("• Tell me something interesting")
    print("• What is Machine Learning?")
    print("\nType 'bye' or 'exit' to end.\n")

    while True:
        user_input = input("Ask me: ").strip()
        if user_input.lower() in ["bye", "exit"]:
            print(chat_pairs["bye"])
            break

        processed_input = preprocess(user_input)
        processed_keys = [preprocess(key) for key in chat_pairs.keys()]
        match = get_best_match(processed_input, processed_keys)

        if match:
            original_key = list(chat_pairs.keys())[processed_keys.index(match)]
            response = chat_pairs[original_key]
            print(f"\n✨ Here's what I found:\n{response}\n")
        else:
            print("\n😕 Hmm... I didn’t get that. Try asking in a different way!\n")

chatbot()
