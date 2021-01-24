import os


def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("not valid template path: %s" %(file_path))
    return file_path

def get_template(path):
    file_path = os.path.join(os.getcwd(), path)
    return open(file_path).read()

def render_context(template_string,context):
    return template_string.format(**context)



file_= "hungryPy\\templates\\email_message.txt"
file_html =  "hungryPy\\templates\\email_message.html"
template_text = get_template(file_html)
context = {
    "name":"Justin",
    "date":"abc",
    "total": 99.91
}
print(render_context(template_text,context))