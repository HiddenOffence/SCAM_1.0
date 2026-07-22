from flask import Flask, render_template

app = Flask(__name__)

questions = [
    {
        "category": "Learning Style",
        "question": "When learning something new, I prefer to:",
        "answers": [
            "Watch videos or diagrams",
            "Listen to explanations or discussions",
            "Do hands-on activities or experiments",
            "Read articles or textbooks"
        ]
    }
]


@app.route("/")
def home():
    return render_template(
        "quiz.html",
        question=questions[0]
    )


if __name__ == "__main__":
    app.run(debug=True)
