
# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data objects
news_items = [
    {
        "id": 1,
        "title": "News Item 1",
        "content": "Content of News Item 1",
        "image": "image1.jpg",
        "date": "2023-03-08"
    },
    {
        "id": 2,
        "title": "News Item 2",
        "content": "Content of News Item 2",
        "image": "image2.jpg",
        "date": "2023-03-09"
    },
    {
        "id": 3,
        "title": "News Item 3",
        "content": "Content of News Item 3",
        "image": "image3.jpg",
        "date": "2023-03-10"
    }
]

# Routes
@app.route("/")
def home():
    return render_template("index.html", news_items=news_items)

@app.route("/news_item_detail/<int:id>")
def news_item_detail(id):
    news_item = next((item for item in news_items if item["id"] == id), None)
    return render_template("news_item.html", news_item=news_item)

# Placeholder routes for post, edit, and delete functionality
@app.route("/post_news_item")
def post_news_item():
    return "Post News Item"

@app.route("/edit_news_item/<int:id>")
def edit_news_item(id):
    return "Edit News Item"

@app.route("/delete_news_item/<int:id>")
def delete_news_item(id):
    return "Delete News Item"

if __name__ == "__main__":
    app.run(debug=True)
