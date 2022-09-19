from flask import Flask, render_template, request, flash, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
import datetime


app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@localhost/db_name"
app.config["SECRET_KEY"] = "super-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/MATH_WORLD_DB"
db = SQLAlchemy(app)
app.config["UPLOAD_FOLDER"] = "./static/post_image/"

app.add_url_rule('/post_image/<path:filename>', endpoint='post_image', view_func=app.send_static_file)
app.add_url_rule('/author_image/<path:filename>', endpoint='author_image', view_func=app.send_static_file)


def text_to_html(string):
    stringList = string.split("\n")
    stringList = [f"<p>{i}</p>" for i in stringList]
    return "\n".join(stringList)

def convert_to_slug(string):
    return "".join([i for i in string.replace(" ", "-") if i.isalnum() or i=="-"])

def read_post(path):
    with open(path, "r", encoding="utf8") as file:
        return file.readlines()


class Contacts(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=True)
    message = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

class Posts(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    first30letters = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String, nullable=False)
    imageurl = db.Column(db.String, nullable=False)
    aid = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)

class Authors(db.Model):
    aid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)


no_of_post_per_page = 4
#max_page = 


@app.before_request
def make_session_permanent():
    session.permanent = True
    #app.permanent_session_lifetime = datetime.timedelta(minutes=5)


@app.route("/")
def homePage():
    postsNauthors = sorted(db.session.query(Posts, Authors).outerjoin(Authors, Posts.aid == Authors.aid).all(), reverse=True, key=lambda x: x[0].pid)

    return render_template("index.html", titleVal="Math World", headerVal = "Math World", headerImg="header-bg.jpg", postsNauthors=postsNauthors, username=session.get("USERNAME"), uid=session.get("USERID"))


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        pass
    
    elif request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg = request.form.get('message')
        
        entry = Contacts(name=name, email=email, phone=phone, message=msg, date=dt.now())
        db.session.add(entry)
        db.session.commit()
    
    return render_template("contact.html", titleVal="Contact", headerVal = "Contact Math World", headerImg="header-bg.jpg")


@app.route("/post/<string:slug>")
def displayPost(slug):
    blogpost = Posts.query.filter_by(slug=slug).first()
    author = Authors.query.filter_by(aid=blogpost.aid).first()
    return render_template('post.html', post=blogpost, author=author, titleVal=blogpost.title, headerVal=blogpost.title, lines=read_post(f"post_content/{blogpost.slug}.txt"), headerImg="header-bg.jpg")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        pass
    
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        username = request.form.get('username')
        password = request.form.get('password')
        description = request.form.get('about')
        
        test = Authors.query.filter_by(email=email).first()
        if test is None:
            entry = Authors(name=name, email=email, phone=phone, username=username.lower(), password=password, description=description)
            db.session.add(entry)
            db.session.commit()
            flash("Wow! You are registered!!")
            return redirect(url_for('register'))
    
    return render_template('register.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        pass
    
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('rememberMe')
        
        author = Authors.query.filter_by(email=email, password=password).first()
        if author is not None:
            session["USERNAME"] = author.username
            session["USERID"] = author.aid
            return redirect("/")
    
    return render_template('login.html')


@app.route("/logout")
def logout():
    session["USERNAME"] = ""
    session["USERID"] = ""
    return redirect("/")


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if request.method == "GET":
        if str(session.get("USERID")) == "1":
            authors = Authors.query.all()
            contacts = Contacts.query.all()
            postsNauthors = db.session.query(Posts, Authors).outerjoin(Authors, Posts.aid == Authors.aid).all()
            return render_template('dashboard.html', authors=authors, contacts=contacts, postsNauthors=postsNauthors)
            
        else:
            return "<h1>404 Error</h1>"
    else:
        posts = Posts.query.filter_by(aid=session["USERID"])
        for post in posts:
            try:
                request.form[str(post.pid)]
                p_id = post.pid
                break
            except:
                continue
        print(f"p_id = {p_id}")
        post = Posts.query.filter_by(pid=int(p_id)).all()[0]
        print(post)
        db.session.delete(post)
        db.session.commit()
        return redirect("/dashboard")


@app.route("/createPost", methods=['GET', 'POST'])
def createPost():
    if str(session.get("USERID")):
        if request.method == "GET":
            pass
        elif request.method == "POST":
            
            pid = int(sorted(Posts.query.all(), reverse=True, key=lambda x: x.pid)[0].pid) + 1
            file = request.files.get('file1')
            print(file)
            title = request.form.get('title')
            content = request.form.get('content')
            first30letters = content[:30]
            slug = convert_to_slug(title)
            imageurl = f"{slug}.jpg" if file else "default.jpg"
            aid = session.get("USERID")
            with open(f"./post_content/{slug}.txt", "w") as f:
                f.write(content)
            
            print(app.config["UPLOAD_FOLDER"] + imageurl)
            if file or file != "default.jpg":
                request.files.get('file1').save(app.config["UPLOAD_FOLDER"] + imageurl)

            new_post = Posts(title=title, first30letters=first30letters, slug=slug, imageurl=imageurl, aid=aid, date=dt.now())
            db.session.add(new_post)
            db.session.commit()

            return redirect("/")
            
        return render_template('createPost.html')
    else:
        return "<h1>404 Error</h1>"


@app.route("/author/<int:a_id>")
def author(a_id):
    try:
        author = Authors.query.filter_by(aid=a_id).all()[0]
        return render_template("author.html", author=author)
    except:
        return "<h1>404 Error</h1>"


@app.route("/blogs", methods=['GET', 'POST'])
def blogs():
    if request.method == "GET":
        posts = Posts.query.filter_by(aid=session["USERID"]).all()
        return render_template("blogs.html", author=session["USERNAME"], posts=posts)
    else:
        posts = Posts.query.filter_by(aid=session["USERID"])
        for post in posts:
            try:
                request.form[str(post.pid)]
                p_id = post.pid
                break
            except:
                continue
        print(f"p_id = {p_id}")
        post = Posts.query.filter_by(pid=int(p_id)).all()[0]
        print(post)
        db.session.delete(post)
        db.session.commit()
        return redirect("/blogs")


if __name__ == "__main__":
    app.run(debug=True)