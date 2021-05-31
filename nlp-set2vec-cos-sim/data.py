training_qs = [
    "What is your name", "hello", "tell me your name?", "what do you do?",
    "locations", "thank you so much", "where do you live"
]
answers = ["chatbot", "hi", "chatbot", "I chat", "India", "welcome", "India"]

user_qs = [
    "name?", "enlighten me with your name", "what kind of work you do",
    "where do you locate yourself", "Hello"
]
user_answers = ["chatbot", "chatbot", "I chat", "India", "hi"]

assert (len(training_qs) == len(answers))
assert (len(user_qs) == len(user_answers))
