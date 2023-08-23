# Flask Blog Application

The Flask Blog Application is a web-based platform that allows users to create, view, update, and delete blog posts. It
is built using the Flask framework, which is a micro web framework for Python. This application provides a user-friendly
interface for managing blog content and interacting with a JSON-based backend data storage.

---

## Features

- View existing blog posts on the homepage.
- Add new blog posts through a user-friendly form.
- Update and edit existing blog posts.
- Delete unwanted blog posts.

---

## Getting Started

1. **Clone the Repository:** Clone this repository to your local machine using the following command:

```bash 
git clone <repository-url>
```

2. **Run the Application:** Start the Flask development server using the following command:

```bash 
python app.py
```

3. **Access the Application:** Open your web browser and go to `http://localhost:5000` to access the application.

---

## Usage

- Homepage (`/`): View all existing blog posts. You can also access the update and delete options for each post.
- Add New Post (`/add`): Fill out the form to add a new blog post. Submitting the form will store the post in the
  database and redirect you to the homepage.
- Update Post (`/update/<post_id>`): Edit an existing blog post. After submitting the form, the updated post will be
  stored in the database, and you will be redirected to the homepage.
- Delete Post (`/delete/<post_id>`): Delete an existing blog post. The post will be immediately removed from the
  database, and you will be redirected to the homepage.

---

## Data Storage

The blog posts are stored in a JSON file (`data/blog_data.json`) for demonstration purposes. In a production
environment, a proper database system should be used.
