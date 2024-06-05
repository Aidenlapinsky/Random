import random

def generate_random_css():
    styles = ["color", "background-color", "font-size"]
    values = ["red", "blue", "green", "yellow", "24px", "36px"]
    css = ""
    for _ in range(random.randint(1, 5)):
        style = random.choice(styles)
        value = random.choice(values)
        css += f"{style}: {value};\n"
    return css

def generate_random_head():
    head = "<style>\n"
    head += generate_random_css()
    head += "</style>\n"
    return head
