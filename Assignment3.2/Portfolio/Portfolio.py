from flask import Flask
from flask import render_template, request, redirect
from Parser import parser
from mongoengine import *
from schemas import CommentPage, Comment, Reply, FruityWord
from time import strftime
import re
from bson.objectid import ObjectId
"""
Flask app and routes. Starts the app and passes the relevant dictionaries to the Jinja2 templates
Also now featuring managing the MongoDB as well as posting new comments and replies, and also 
handling expletive filtering
"""

app = Flask(__name__)
projects = parser.parse_files()


@app.route('/')
def start_page():
    return render_template('index.html', projects=projects)


@app.route('/<project_name>')
def access_project(project_name=None):
    return render_template('project_page.html', project_name=project_name, project=projects[project_name])


@app.route('/<project>/<file_name>', methods=['GET'])
def access_subdirectory(project=None, file_name=None):
    is_file = request.args.get("is_file")
    current_directory = projects
    project_dirs = project.split('_')
    for dirs in project_dirs:
        current_directory = current_directory[dirs]

    if is_file == 'True':
        comment_page = CommentPage.objects.filter(file_path=current_directory[file_name]['path']).first()
        if comment_page is not None:
            comments = comment_page.comments
        else:
            comments = None

        if comments is not None:
            comments = sorted(comments, key=get_votes, reverse=True)
            for comment in comments:
                comment.replies = sorted(comment.replies, key=get_votes, reverse=True)

        return render_template('file_page.html', file_name=file_name, project_name=project,
                               file_data=current_directory[file_name], comments=comments)
    else:
        project_path = project + '_' + file_name
        return render_template('project_page.html', project_name=project_path, project=current_directory[file_name])


@app.route('/<project>/<file_name>/sort', methods=['GET'])
def access_subdirectory2(project=None, file_name=None):
    is_file = request.args.get("is_file")
    current_directory = projects
    project_dirs = project.split('_')
    for dirs in project_dirs:
        current_directory = current_directory[dirs]

    if is_file == 'True':
        comment_page = CommentPage.objects.filter(file_path=current_directory[file_name]['path']).first()
        if comment_page is not None:
            comments = comment_page.comments
        else:
            comments = None

        if comments is not None:
            comments = sorted(comments, key=get_replies, reverse=True)
            for comment in comments:
                comment.replies = sorted(comment.replies, key=get_votes, reverse=True)

        return render_template('file_page.html', file_name=file_name, project_name=project,
                               file_data=current_directory[file_name], comments=comments)
    else:
        project_path = project + '_' + file_name
        return render_template('project_page.html', project_name=project_path, project=current_directory[file_name])


@app.route('/revisions/<project>/<file_name>', methods=['GET'])
def access_revisions(project=None, file_name=None):
    current_directory = projects
    project_dirs = project.split("_")
    for dirs in project_dirs:
        current_directory = current_directory[dirs]
    revisions = current_directory[file_name]['revisions']
    return render_template('revisions_page.html', revisions=revisions, file_name=file_name)


@app.route('/<project>/<file_name>', methods=['POST'])
def post_comment(project=None, file_name=None):
    is_reply = request.form.get('is_reply')
    is_vote = request.form.get('is_vote')
    if is_vote == 'True':
        file_path = request.form.get('file_path')
        this_id = request.form.get('id')
        value = request.form.get('value')
        comment_page = CommentPage.objects.filter(file_path=file_path).first()
        if comment_page is None:
            comment_page = CommentPage(file_path=file_path)
        if is_reply == 'True':
            for acomment in comment_page.comments:
                for reply in acomment.replies:
                    if str(reply.my_id) == str(this_id):
                        if value == 'up':
                            reply.votes += 1
                        else:
                            reply.votes -= 1
            comment_page.save()
        else:
            for comment in comment_page.comments:
                if str(comment.my_id) == str(this_id):
                    if value == 'up':
                        comment.votes += 1
                    else:
                        comment.votes -= 1
            comment_page.save()

    elif is_reply == 'True':
        file_path = request.form.get('file_path')
        parent = int(request.form.get('parent'))
        username = request.form.get('username')
        comment_text = clean_comment(request.form.get('comment_text'))
        timestamp = strftime("%Y-%m-%d %H:%M:%S")

        reply = Reply(username=username, comment_text=comment_text, timestamp=timestamp, votes=0, my_id=ObjectId())
        comment_page = CommentPage.objects.filter(file_path=file_path).first()
        parent = comment_page.comments[parent]
        parent.replies.append(reply)
        comment_page.save()

    else:
        file_path = request.form.get('file_path')
        username = request.form.get('username')
        comment_text = clean_comment(request.form.get('comment_text'))
        timestamp = strftime("%Y-%m-%d %H:%M:%S")

        comment = Comment(username=username, comment_text=comment_text, timestamp=timestamp, votes=0, my_id=ObjectId())
        comment_page = CommentPage.objects.filter(file_path=file_path).first()
        if comment_page is None:
            comment_page = CommentPage(file_path=file_path)
        comment_page.comments.append(comment)
        comment_page.save()

    return redirect('/' + project + '/' + file_name + '?is_file=True')


@app.route('/<project>/<file_name>/sort', methods=['POST'])
def post_comment2(project=None, file_name=None):
    is_reply = request.form.get('is_reply')
    is_vote = request.form.get('is_vote')
    if is_vote == 'True':
        file_path = request.form.get('file_path')
        this_id = request.form.get('id')
        value = request.form.get('value')
        comment_page = CommentPage.objects.filter(file_path=file_path).first()
        if comment_page is None:
            comment_page = CommentPage(file_path=file_path)
        if is_reply == 'True':
            for acomment in comment_page.comments:
                for reply in acomment.replies:
                    if str(reply.my_id) == str(this_id):
                        if value == 'up':
                            reply.votes += 1
                        else:
                            reply.votes -= 1
            comment_page.save()
        else:
            for comment in comment_page.comments:
                if str(comment.my_id) == str(this_id):
                    if value == 'up':
                        comment.votes += 1
                    else:
                        comment.votes -= 1
            comment_page.save()

    elif is_reply == 'True':
        file_path = request.form.get('file_path')
        parent = int(request.form.get('parent'))
        username = request.form.get('username')
        comment_text = clean_comment(request.form.get('comment_text'))
        timestamp = strftime("%Y-%m-%d %H:%M:%S")

        reply = Reply(username=username, comment_text=comment_text, timestamp=timestamp, votes=0, my_id=ObjectId())
        comment_page = CommentPage.objects.filter(file_path=file_path).first()
        parent = comment_page.comments[parent]
        parent.replies.append(reply)
        comment_page.save()

    else:
        file_path = request.form.get('file_path')
        username = request.form.get('username')
        comment_text = clean_comment(request.form.get('comment_text'))
        timestamp = strftime("%Y-%m-%d %H:%M:%S")

        comment = Comment(username=username, comment_text=comment_text, timestamp=timestamp, votes=0, my_id=ObjectId())
        comment_page = CommentPage.objects.filter(file_path=file_path).first()
        if comment_page is None:
            comment_page = CommentPage(file_path=file_path)
        comment_page.comments.append(comment)
        comment_page.save()

    return redirect('/' + project + '/' + file_name + '/sort?is_file=True')


def clean_comment(comment=""):
    """
    Returns a cleaned version of the comment. Splits comment and matches each word against the
    database. Replaces it with the alternative if found.
    """
    word_list = comment.split()
    clean_word = []
    for word in word_list:
        # http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        alpha_word = re.sub(r'\W+', '', word).lower()
        nice_word = FruityWord.objects(fruity_word=alpha_word).first()
        if nice_word is not None:
            clean_word.append(nice_word.less_fruity_word)
        else:
            clean_word.append(word)

    cleaned_comment = " ".join(clean_word)
    return cleaned_comment


def get_votes(comment):
    return comment.votes


def get_replies(comment):
    return len(comment.replies)

if __name__ == '__main__':
    connect('assignment3db')
    app.run()
