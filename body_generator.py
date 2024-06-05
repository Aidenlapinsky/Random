import random

def generate_random_text():
    words = ["hello", "world", "random", "website", "github"]
    text = ""
    for _ in range(random.randint(1, 10)):
        word = random.choice(words)
        text += f"{word} "
    return text

def generate_random_body():
    body = "<p id='foo'>"
    body += generate_random_text()
    body += "</p>\n"
    return body
