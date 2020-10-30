from flask import Flask,  render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default="N/A")
    date_posted =db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog Post ' + str(self.id)

db.create_all()
# all_posts =[
# {
#     'title': 'Post 1',
#     'content': 'This is the content of post 1',
#     'author': 'John Elesho'
# },
# {
#     'title': 'Post 2',
#     'content': 'This is the content of post two'
# },
# ]

@app.route('/', methods=['GET', 'POST'])
def post():
    all_posts_from_db = BlogPost.query.all()
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('post.html', posts = all_posts_from_db)



if __name__ == "__main__":
    app.run(debug=True)





