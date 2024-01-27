words = [
    "tough", "toward", "town", "trade", "traditional", "training", "travel", "treat", "treatment", "tree",
    "trial", "trip", "trouble", "true", "truth", "try", "turn", "TV", "two", "type", "under", "understand",
    "unit", "until", "up", "upon", "us", "use", "usually", "value", "various", "very", "victim", "view",
    "violence", "visit", "voice", "vote", "wait", "walk", "wall", "want", "war", "watch", "water", "way",
    "we", "weapon", "wear", "week", "weight", "well", "west", "western", "what", "whatever", "when", "where",
    "whether", "which", "while", "white", "who", "whole", "whom", "whose", "why", "wide", "wife", "will",
    "win", "wind", "window", "wish", "with", "within", "without", "woman", "wonder", "word", "work", "worker",
    "world", "worry", "would", "write", "writer", "wrong", "yard", "yeah", "year", "yes", "yet", "you",
    "young", "your", "yourself"
]

with open("wordBank.txt", "w") as file:
    for word in words:
        file.write(word + "\n")
