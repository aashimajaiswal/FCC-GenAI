import os
import re
from flask import Flask, render_template, request
from helper import llm_pipeline  # Make sure your helper module provides llm_pipeline

app = Flask(__name__)

# Configure the upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def remove_markdown(text):
    """
    Removes markdown formatting (bold, italics) from the given text.
    """
    text = re.sub(r"\*\*\*(.*?)\*\*\*", r"\1", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    return text

def format_numbered_list(text):
    """
    Converts numbered lists in the text into HTML ordered lists.
    Detects lines starting with a number followed by a period and a space.
    """
    lines = text.splitlines()
    new_lines = []
    list_lines = []
    for line in lines:
        if re.match(r'^\s*\d+\.\s+', line):
            list_lines.append(line.strip())
        else:
            if list_lines:
                # Convert accumulated list lines into an HTML ordered list
                list_html = "<ol>" + "".join([
    "<li>{}</li>".format(re.sub(r'^\d+\.\s+', '', l)) for l in list_lines
]) + "</ol>"
                new_lines.append(list_html)
                list_lines = []
            new_lines.append(line)
    if list_lines:
        list_html = "<ol>" + "".join(
            f"<li>{re.sub(r'^\d+\.\s+', '', l)}</li>" for l in list_lines
        ) + "</ol>"
        new_lines.append(list_html)
    return "\n".join(new_lines)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve the file and topic from the form
        file = request.files.get("file")
        topic = request.form.get("topic")
        
        if file and topic:
            # Save the file to the upload folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            
            # Call your pipeline to get the answer chain and generated questions
            ans_chain, ques_list = llm_pipeline(file_path, topic)
            
            # Build QA pairs by running each question through the answer chain
            qa_pairs = []
            for question in ques_list:
                answer = ans_chain.run(question)
                # First remove markdown formatting
                cleaned_answer = remove_markdown(answer)
                # Then convert numbered points into HTML ordered lists
                formatted_answer = format_numbered_list(cleaned_answer)
                qa_pairs.append({"question": question, "answer": formatted_answer})
            
            # Render the result page with file info and QA pairs
            return render_template("result.html", file_path=file_path, topic=topic, qa_pairs=qa_pairs)
        else:
            error_message = "Missing file or topic. Please try again."
            return render_template("index.html", error=error_message)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
