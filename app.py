from flask import *
import json

# Flask, render_template, request, redirect, url_for

BLOG_DATA_PATH = "data/blog_data.json"


def parse_json(data):
    """
    Parse JSON file in to Python object.
    """
    with open(data, "r") as f:
        return json.load(f)


def modify_json(file_path, data):
    """
    Save modified data to file.
    """
    with open(file_path, "w") as f:
        json.dump(data, f)


app = Flask(__name__)


@app.route("/")
def index():
    """Handles homepage requests"""
    blog_posts = parse_json(BLOG_DATA_PATH)
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Shows form when website is reached via GET request to add new blog posts
    After filling out form and submitting:
        - new blog post will be added to database
        - user will be redirected to homepage to see the new added post
    """
    if request.method == 'POST':
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        blog_posts = parse_json(BLOG_DATA_PATH)

        new_blog_post = {
            "id": len(blog_posts) + 1,
            "author": author,
            "title": title,
            "content": content
        }
        print(blog_posts)
        blog_posts.append(new_blog_post)
        modify_json(BLOG_DATA_PATH, blog_posts)

        return redirect(url_for("index"))
    return render_template('add.html')


if __name__ == "__main__":
    app.run()
