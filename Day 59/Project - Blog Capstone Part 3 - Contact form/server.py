from flask import Flask, render_template, url_for, request
from  functions import send_mail, get_data


app = Flask(__name__)



@app.route("/")
def home():
    url_blog=url_for("blog")
    blog_posts = get_data("https://api.npoint.io/af5bab5af8fdc5d07270")
    newest_posts= blog_posts[-6:]
    return render_template("index.html", url_blog=url_blog, posts=newest_posts)


@app.route("/blog")
def blog():
    blog_posts = get_data("https://api.npoint.io/af5bab5af8fdc5d07270")
    url_blog = url_for("blog")
    return render_template("blog.html",posts=blog_posts, url_blog=url_blog, input_video="./static/videos/blogpage.mp4",
        input_text="Djur som Överraskar – Saker du inte visste")


@app.route("/blog/<int:id>")
def blog_post(id):
    blog_posts = get_data("https://api.npoint.io/af5bab5af8fdc5d07270")
    # Filtrera ut posten som en lista med ett element
    post = [item for item in blog_posts if item["id"] == id]

    return render_template("post.html", post=post[0])


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        # Hämta användarens e-post och meddelande från formuläret
        from_email = request.form["email"]
        input_message = request.form["message"]
        # Om båda fälten är ifyllda, skicka email
        if input_message and from_email:
            send_mail(from_email, input_message)


    return render_template("contact.html",  input_video="./static/videos/contact.mp4",
                input_text="Kontakt" )




if __name__ == "__main__":
    app.run(debug=True)