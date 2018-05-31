from flask import request
from lidarts import socketio, db
from flask_login import current_user
from lidarts.socket.chat_handler import broadcast_online_players
from datetime import datetime


@socketio.on('connect', namespace='/base')
def connect():
    print('Client connected', request.sid)
    if current_user.is_authenticated:
        current_user.active_sessions += 1
        db.session.commit()
        broadcast_online_players()


@socketio.on('user_heartbeat', namespace='/base')
def connect():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.commit()
        broadcast_online_players()


@socketio.on('disconnect', namespace='/base')
def disconnect():
    print('Client disconnected', request.sid)
    if current_user.is_authenticated:
        current_user.active_sessions -= 1
        db.session.commit()
        broadcast_online_players()