from mongoengine import *
"""
Schemas for the MongoDB database. Uses MongoEngine declarations.
Each page is a document, with nested comments and each comment
having nested replies.
The expletive collection is called FruityWord, with each document
having two fields, the word to find and the word to replace it
with
"""


class Reply(Document):
    username = StringField()
    comment_text = StringField()
    timestamp = StringField()


class Comment(Document):
    username = StringField()
    comment_text = StringField()
    timestamp = StringField()
    replies = ListField(EmbeddedDocumentField('Reply'))


class CommentPage(Document):
    file_path = StringField()
    comments = ListField(EmbeddedDocumentField('Comment'))


class FruityWord(Document):
    fruity_word = StringField()
    less_fruity_word = StringField()
