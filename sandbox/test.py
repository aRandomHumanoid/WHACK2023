from marshmallow import Schema, fields

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
    title = fields.Str
    author = fields.Str
    description = fields.Str
    image = fields.Str
    location = fields.Str

    def make_post(self, data, **kwargs):
        return Post(**data)

all_posts = [Post("hi", "me", "a nice place", "", "nowhere."), Post("heyy", "me", "a nice place", "", "nowhere.")]

schema = PostSchema(many=True)
print(schema.dump(all_posts))