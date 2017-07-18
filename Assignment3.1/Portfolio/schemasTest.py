from mongoengine import *
from schemas import CommentPage, Comment, Reply
"""
Simple test script to check the creation of collections 
and whether the schema is working
"""


connect('assignment3db')
commentpage1 = CommentPage(file_path='testlink')
comment1 = Comment(username = "Shrujan", comment_text="Yo Yo Yo", timestamp="4:20")
reply1 = Reply(username = "Shrujan", comment_text="Yo Yo Yo", timestamp="4:20")

commentpage1.comments.append(comment1)
comment1.replies.append(reply1)

commentpage1.save()
