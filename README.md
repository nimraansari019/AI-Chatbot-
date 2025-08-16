
#  NLP Chatbot using NLTK

##  Project Overview

This project implements a simple **chatbot** using **Natural Language Processing (NLP)** concepts with the help of **NLTK (Natural Language Toolkit)** in Python. The chatbot is designed to answer basic queries related to Python, Artificial Intelligence (AI), and Machine Learning (ML). It demonstrates how rule-based chatbots can be created using preprocessing, lemmatization, and fuzzy matching.

The chatbot runs in a terminal or Python IDLE environment, where the user can type queries, and the bot responds intelligently. The project focuses on **text preprocessing and response generation** instead of using heavy machine learning models, making it easy for beginners to understand.

---

##  Tools & Libraries Used

1. **Programming Language:** Python 3.12

2. **Libraries:**

   * **NLTK** → Used for NLP tasks like tokenization and lemmatization.
   * **difflib** → For fuzzy string matching (so even if the user types a slightly different query, the bot can still understand).
   * **Regex (re)** → For simple text tokenization.

3. **Platform Used:**

   * The chatbot was developed and tested in **Python IDLE** and can also run in **terminal/command prompt**.

---

## 🛠 How the Chatbot Works

1. **Preprocessing User Input:**

   * The input is cleaned (punctuation removed, converted to lowercase).
   * Stopwords are removed, and words are lemmatized (e.g., "learning" → "learn").

2. **Matching User Queries:**

   * A dictionary (`chat_pairs`) is defined with predefined questions and answers.
   * The user’s query is compared with available keys using **fuzzy matching**.
   * If a match is found, the chatbot returns the response.

3. **Response Handling:**

   * If the query is recognized → chatbot gives the correct answer.
   * If not recognized → chatbot politely asks the user to rephrase.
   * If the user types `"bye"` or `"exit"` → chatbot says goodbye and ends the conversation.

---

##  Example Interaction

```
🤖 Welcome to NLP Chatbot!
You can ask me things like:
• What is Python?
• Who created Python?
• What is AI?
• Tell me something interesting
• What is Machine Learning?

Type 'bye' or 'exit' to end.

Ask me: what is python
✨ Here's what I found:
Python is a popular programming language.

Ask me: who created python
✨ Here's what I found:
Guido van Rossum created Python in 1991.

Ask me: bye
Goodbye! Have a nice day 💖
```
Output:
<img width="1536" height="889" alt="Image" src="https://github.com/user-attachments/assets/30be2b1c-d594-4f27-9c12-972e4827a731" />


##  Applications

* **Education:** Students can use simple chatbots to learn programming basics.
* **Customer Support:** Can be extended to FAQs for small businesses.
* **Personal Assistants:** Basis for building personal AI helpers.
* **NLP Learning Projects:** Great for beginners to practice NLP libraries.

---



##  Conclusion

This chatbot demonstrates how **rule-based chatbots** can be implemented using **NLTK** for natural language processing and **fuzzy matching** for flexibility. Although simple, it shows the foundation of how conversational agents work. This project can be expanded with advanced NLP libraries like **spaCy** or deep learning models for more realistic conversations.

---




