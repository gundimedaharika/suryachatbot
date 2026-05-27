from flask import Flask, render_template, request

import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

app = Flask(__name__)

# Your Python function
def process_text(user_input):
    return user_input.upper()

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7,
        api_key=os.getenv("GROQ_API_KEY")
    )

    if request.method == "POST":
        question = request.form["input_text"]
        messages = [
            SystemMessage(content="You are a good assistant."),
            # HumanMessage(content="What is the capital of Japan.")
            HumanMessage(content=question)
        ]
        response = llm.invoke(messages)
        output = response.content

    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)