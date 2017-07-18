from flask import Flask
from flask import jsonify
from flask import make_response
from flask import abort
from flask import request
import json
import requests
"""
The API for our data set
Includes Get, Put, Post and Delete
"""


app = Flask(__name__)

"""
Retrieve the json from github
"""
r = requests.get('https://raw.githubusercontent.com/shrujancheruku/Test/master/data.json')
lists = r.json()

actor_list = lists[0]
actor_name_list = []
for actor in actor_list:
    actor_name_list.append(actor)

movie_list = lists[1]
movie_name_list = []
for movie in movie_list:
    movie_name_list.append(movie)

"""
Usage example: /actors/name/Bruce
returns a JSON with all actors with Bruce in their name's information
"""


@app.route('/actors/<string:attr>/<string:attr_value>', methods=['GET'])
def get_actors(attr, attr_value):

    results_list = []
    if attr in actor_list[actor_name_list[0]]:
        for actor in actor_name_list:
            if attr_value in str(actor_list[actor][attr]):
                results_list.append(actor_list[actor])
    if len(results_list) is not 0:
        return jsonify(results_list)

    abort(400)

"""
Usage example: movies/name/Blind
returns a JSON with all movies with Blind in their name's information
"""


@app.route('/movies/<string:attr>/<string:attr_value>', methods=['GET'])
def get_movies(attr, attr_value):

    results_list = []
    if attr in movie_list[movie_name_list[0]]:
        for movie in movie_name_list:
            if attr_value in str(movie_list[movie][attr]):
                results_list.append(movie_list[movie])
    if len(results_list) is not 0:
        return jsonify(results_list)

    abort(400)

"""
Usage example:/actors/Bruce Willis
returns a JSON with Bruce Willis's information
"""


@app.route('/actors/<string:name>', methods=['GET'])
def get_actor(name):

    for actor in actor_name_list:
        if name == actor_list[actor]['name']:
            return jsonify(actor_list[actor])

    abort(400)

"""
Usage example:/movies/Blind Date
returns a JSON with Blind Date's information
"""


@app.route('/movies/<string:name>', methods=['GET'])
def get_movie(name):

    for movie in movie_name_list:
        if name == movie_list[movie]['name']:
            return jsonify(movie_list[movie])

    abort(400)

"""
Usage example:/actors/Bruce Willis, {'total_gross': 50000}
updates the actor with the fields in the given JSON
"""


@app.route('/actors/<string:name>', methods=['PUT'])
def put_actor(name):
    if not request.json:
        abort(400)

    if name not in actor_list:
        abort(400)

    for item in request.json:
        if item not in actor_list[name]:
            abort(400)
        else:
            actor_list[name][item] = request.json[item]

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


"""
Usage example:/movies/Blind Date, {'year': 2017}
updates the movie with the fields in the given JSON
"""


@app.route('/movies/<string:name>', methods=['PUT'])
def put_movie(name):
    if not request.json:
        abort(400)

    if name not in movie_list:
        abort(400)

    for item in request.json:
        if item not in movie_list[name]:
            abort(400)
        else:
            movie_list[name][item] = request.json[item]

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

"""
Usage example:/actors/, {
                            'name': 'Matt Damon'
                            'age': 50
                        }
creates a new actor with the fields in the given JSON
name is required and cannot already exist
"""


@app.route('/actors/', methods=['POST'])
def post_actor():
    if not request.json or 'name' not in request.json:
        abort(400)

    if request.json['name'] in actor_list:
        abort(400)

    actor_list[request.json['name']] = request.json
    actor_name_list.append(request.json['name'])

    return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}

"""
Usage example:/moviess/, {
                            'name': 'Invictus'
                            'year': 2010
                        }
creates a new movie with the fields in the given JSON
name is required and cannot already exist
"""


@app.route('/movies/', methods=['POST'])
def post_movie():
    if not request.json or 'name' not in request.json:
        abort(400)

    if request.json['name'] in movie_list:
        abort(400)

    movie_list[request.json['name']] = request.json
    movie_name_list.append(request.json['name'])

    return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}

"""
Usage example:/actors/, {
                            'name': 'Bruce Willis'
                            'age': 6
                        }
deletes an actor based on the name field in the provided JSON
name is required and must already exist
"""


@app.route('/actors/', methods=['DELETE'])
def delete_actor():
    if not request.json or 'name' not in request.json:
        abort(400)

    if request.json['name'] not in actor_list:
        abort(400)

    del actor_list[request.json['name']]
    actor_name_list.remove(request.json['name'])

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

"""
Usage example:/movies/, {
                            'name': 'Blind Date'
                            'year': 1987
                        }
deletes a movie based on the name field in the provided JSON
name is required and must already exist
"""


@app.route('/movies/', methods=['DELETE'])
def delete_movie():
    if not request.json or 'name' not in request.json:
        abort(400)

    if request.json['name'] not in movie_list:
        abort(400)

    del movie_list[request.json['name']]
    movie_name_list.remove(request.json['name'])

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

"""
Error handlers for HTTP errors 400, 404 and 500.
Provides JSON output for easier feedback
"""


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'You broke me :'}), 500)


if __name__ == '__main__':
    app.run()
