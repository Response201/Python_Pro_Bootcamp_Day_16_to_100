from flask import Flask, render_template, url_for
import requests
#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)


app = Flask(__name__)

def get_data(url):
    res = requests.get(url)
    res.raise_for_status()
    return res.json()


@app.route("/")
def home():
    url_blog=url_for("blog")
    blog_posts = get_data("https://api.npoint.io/af5bab5af8fdc5d07270")
    newest_posts= blog_posts[-6:]
    return render_template("index.html", url_blog=url_blog, newest_posts=newest_posts)


@app.route("/blog")
def blog():
    blog_posts = get_data("https://api.npoint.io/af5bab5af8fdc5d07270")
    url_blog = url_for("blog")
    return render_template("blog.html",posts=blog_posts, base_url=url_blog)


@app.route("/blog/<int:id>")
def blog_post(id):
    blog_posts = get_data("https://api.npoint.io/af5bab5af8fdc5d07270")
    # Filtrera ut posten som en lista med ett element
    post = [item for item in blog_posts if item["id"] == id]

    return render_template("post.html", post=post[0])






if __name__ == "__main__":
    app.run()