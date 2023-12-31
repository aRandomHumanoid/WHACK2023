from flask import Flask, jsonify, request

from marshmallow import Schema, fields

app = Flask(__name__)
class Post:
    def __init__(self, title, author, description, image, location):
        self.title = title
        self.author = author
        self.description = description
        self.image = image
        self.location = location

    def __repr__(self):
        return "<Post(title={title.name!r})>".format(self=self)

class PostSchema(Schema):
    title = fields.Str()
    author = fields.Str()
    description = fields.Str()
    image = fields.Str()
    location = fields.Str()

    def make_post(self, data, **kwargs):
        return Post(**data)


all_posts = [Post("hi", "me", "a nice place", "", "nowhere."), Post("heyy", "me", "a nice place", "", "nowhere.")]

@app.route('/posts')
def get_posts():
    schema = PostSchema(many=True)
    out = schema.dumps(all_posts)
    return out


@app.route('/posts', methods=['POST'])
def add_post():
    schema = PostSchema()
    all_posts.append(schema.load(request.get_json()))
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
