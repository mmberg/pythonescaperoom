from flask import Flask, jsonify, render_template, request, abort
from EscapeRoomGame import EscapeRoomGame
import os
import string
import random

app = Flask("")
game = EscapeRoomGame()


@app.route('/')
def index():
    game.reset()
    return render_template('escape.html')


@app.route('/rooms/<string:name>', methods=['POST'])
def load_room(name):
    game.load_room(name)
    return jsonify({"success": True, "room_name": name})


@app.route('/rooms', methods=['POST'])
def load_all_rooms():
    game.load_all_rooms()
    return jsonify({"success": True})


@app.route('/rooms/available')
def get_available_rooms():
    return jsonify(game.find_rooms())


@app.route('/rooms')
def get_loaded_rooms():
    room_names = [room.get_name() for room in game.get_rooms()]
    return jsonify({"count": len(room_names), "room_names": room_names})


@app.route('/rooms/<int:room_nr>')
def get_room(room_nr):
    if(len(game.get_rooms()) <= room_nr):
        #print("Room does not exist.")
        abort(404)
    else:
        return jsonify(game.get_room(room_nr).get_metadata())


@app.route('/rooms/<int:room_nr>/levels')
def get_levels(room_nr):
    return jsonify({"count": len(game.get_rooms()[room_nr].get_levels())})


@app.route('/rooms/<int:room_nr>/levels/<int:level_nr>')
def get_level(room_nr, level_nr):
    room = game.get_rooms()[room_nr]
    levels = room.get_levels()
    if level_nr < len(levels):
        level = room.get_levels()[level_nr]
        return jsonify({"tasks": level["task_messages"], "hints": level["hints"]})
    else:
        #print("Invalid level.")
        abort(404)


@app.route('/rooms/<int:room_nr>/levels/<int:level_nr>/solve', methods=['POST'])
def post_solve_level(room_nr, level_nr):
    room = game.get_rooms()[room_nr]
    level = room.get_levels()[level_nr]
    file = request.files['file']
    filename = ''.join(random.choices(
        string.ascii_lowercase + string.digits, k=7))
    file.save(filename+".py")
    solution = room.check_solution(
        filename, level["solution_function"], level["data"], level.get("algorithm", None))
    os.remove(filename+".py")
    return jsonify(solution)


app.run()
