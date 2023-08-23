from flask import Flask, request, render_template, redirect, url_for
import json
import uuid

app = Flask(__name__)
BLOG_DATA_PATH = "data/blog_data.json"


# Helper Functions
def parse_json(file_path):
    """Parse JSON file to a Python object."""
    with open(file_path, "r") as f:
        return json.load(f)


def fetch_post_by_id(post_id):
    """
    Takes a post ID as arg and Iterates over all blog posts until:
        - No matching post is found -> returns None
        - A matching post is found -> returns that post & its index
    """
    blog_posts = parse_json(BLOG_DATA_PATH)

    for post in blog_posts:
        if post['id'] == post_id:
            return post, blog_posts.index(post)
    return None


def modify_json(file_path, data):
    """Save modified data to JSON file."""
    with open(file_path, "w") as f:
        json.dump(data, f)


# Routes


@app.route("/")
def index():
    """Handles homepage requests"""
    blog_posts = parse_json(BLOG_DATA_PATH)
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Route [/add] to add a new blog post with a UUID.
    Behaviour of route changes depending on request method:

    GET:
        - Initial response: Render add.html -> user can add new post

    POST:
        - Submitting form: Post added to database -> user redirected to root [/]
    """

    if request.method == 'POST':
        blog_posts = parse_json(BLOG_DATA_PATH)
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        new_post = {
            "id": str(uuid.uuid4()),
            "author": author,
            "title": title,
            "content": content
        }

        blog_posts.append(new_post)
        modify_json(BLOG_DATA_PATH, blog_posts)

        return redirect(url_for("index"))
    return render_template('add.html')


@app.route('/delete/<post_id>')
def delete(post_id):
    """
    Deletes post from database and redirects user back to homepage [/].
    Deletion is immediately apparent.
    """
    blog_posts = parse_json(BLOG_DATA_PATH)

    for post in blog_posts:
        if post["id"] == post_id:
            blog_posts.remove(post)
            modify_json(BLOG_DATA_PATH, blog_posts)
            return redirect(url_for("index"))


@app.route('/update/<post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Route [/update<int:post_id>] to update a blog post.
    Behaviour of route changes depending on request method:

    GET:
        - Initial response: Render update.html -> user can update specified post

    POST:
        - After submitting form: Post gets updated -> user redirected to root
    """
    blog_posts = parse_json(BLOG_DATA_PATH)
    specified_post, post_index = fetch_post_by_id(post_id)

    if specified_post is None:
        # Post not found
        return "Post not found", 404

    # Update the post in the JSON file if POST request
    if request.method == 'POST':
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        new_post = {
            "id": post_id,
            "author": author,
            "title": title,
            "content": content
        }

        blog_posts[post_index] = new_post
        modify_json(BLOG_DATA_PATH, blog_posts)

        # Redirect back to index
        return redirect(url_for("index"))

    # Else, it's a GET request
    # Thus displays update.html page
    return render_template('update.html', post=specified_post)


# Main execution
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
