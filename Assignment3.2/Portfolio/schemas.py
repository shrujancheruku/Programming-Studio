from mongoengine import *
from bson.objectid import ObjectId

"""
Schemas for the MongoDB database. Uses MongoEngine declarations.
Each page is a document, with nested comments and each comment
having nested replies.
The expletive collection is called FruityWord, with each document
having two fields, the word to find and the word to replace it
with
"""


class Reply(Document):
    my_id = ObjectIdField(default=ObjectId())
    username = StringField()
    comment_text = StringField()
    timestamp = StringField()
    votes = IntField()


class Comment(Document):
    my_id = ObjectIdField(default=ObjectId())
    username = StringField()
    comment_text = StringField()
    timestamp = StringField()
    replies = ListField(EmbeddedDocumentField('Reply'))
    votes = IntField()


class CommentPage(Document):
    file_path = StringField()
    comments = ListField(EmbeddedDocumentField('Comment'))


class FruityWord(Document):
    fruity_word = StringField()
    less_fruity_word = StringField()
