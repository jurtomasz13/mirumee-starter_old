from sqlite3 import Cursor

from utils import to_json, get_db
from queries import *


@get_db
def create_player(db: Cursor, player_details: dict) -> int:
    db.execute(CREATE_PLAYER, player_details)
    return db.lastrowid


@get_db
def get_player_by_name(db: Cursor, name: str) -> dict:
    player = db.execute(SELECT_PLAYER_BY_NAME, {'name': name}).fetchone()
    return to_json(player)


@get_db
def get_player_by_id(db: Cursor, id: int) -> dict:
    player = db.execute(SELECT_PLAYER_BY_ID, {'rowid': id}).fetchone()
    return to_json(player)


@get_db
def update_stats(db: Cursor, winner: str, loser: str) -> dict:
    db.execute(
        ADD_KILL, {'name': winner})
    db.execute(
        ADD_DEATH, {'name': loser})
    result = {
        'winner': to_json(db.execute(SELECT_PLAYER_BY_NAME, {'name': winner}).fetchone()),
        'loser': to_json(db.execute(SELECT_PLAYER_BY_NAME, {'name': loser}).fetchone())
    }
    return result


@get_db
def get_players(db: Cursor) -> dict:
    players = db.execute(SELECT_ALL_PLAYERS).fetchall()
    return to_json(players)


@get_db
def login(db: Cursor, name: str) -> dict:
    db.execute(SET_ONLINE, {'name': name})
    result = db.execute(SELECT_PLAYER_BY_NAME, {'name': name}).fetchone()
    return to_json(result)


@get_db
def logout(db: Cursor, name: str) -> dict:
    db.execute(SET_OFFLINE, {'name': name})
    result = db.execute(SELECT_PLAYER_BY_NAME, {'name': name}).fetchone()
    return to_json(result)
