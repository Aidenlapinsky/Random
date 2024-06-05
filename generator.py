import head_generator
import body_generator

def generate_random_website():
    html = "<!DOCTYPE html>\n"
    html += "<html>\n"
    html += "<head>\n"
    html += head_generator.generate_random_head()
    html += "</head>\n"
    html += "<body>\n"
    html += body_generator.generate_random_body()
    html += "</body>\n"
    html += "</html>\n"
    return html

with open("index.html", "w") as f:
    f.write(generate_random_website())
