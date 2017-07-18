from flask import Flask
from flask import render_template, request
from Parser import parser
"""
Flask app and routes. Starts the app and passes the relevant dictionaries to the Jinja2 templates
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
    project_dirs = project.split("_")
    for dirs in project_dirs:
        current_directory = current_directory[dirs]
    if is_file == "True":
        return render_template('file_page.html', file_name=file_name, project_name=project,
                               file_data=current_directory[file_name])
    else:
        project_path = project + "_" + file_name
        return render_template('project_page.html', project_name=project_path, project=current_directory[file_name])


@app.route('/revisions/<project>/<file_name>')
def access_revisions(project=None, file_name=None):
    current_directory = projects
    project_dirs = project.split("_")
    for dirs in project_dirs:
        current_directory = current_directory[dirs]
    revisions = current_directory[file_name]["revisions"]
    return render_template('revisions_page.html', revisions=revisions, file_name=file_name)


if __name__ == '__main__':
    app.run()
