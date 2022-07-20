import http

from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError

from database import db
from models.games import Games
from serializers.game import GamesSchema

game_router = Blueprint('game', __name__, url_prefix='/game')


@game_router.route('')
def get():
    games_schema = GamesSchema()

    games = Games.query.order_by(Games.title)
    games_json = games_schema.dump(games, many=True)
    return jsonify(games_json)


@game_router.route('/<int:id_>')
def retrieve(id_):
    games_schema = GamesSchema()
    games = Games.query.filter_by(id=id_).first()
    games_json = games_schema.dump(games)
    return jsonify(games_json)


@game_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = GamesSchema()
    try:
        games_data = schema.load(data)
        new_game = Games(title=games_data['title'])
        db.session.add(new_game)
        db.session.commit()

        new_game_json = schema.dump(new_game)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_game_json


@game_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = GamesSchema()
    try:
        games_data = schema.load(data)
        game = Games.query.filter_by(id=id_).first()
        game.title = games_data['title']
        db.session.add(game)
        db.session.commit()

        new_game_json = schema.dump(game)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_game_json


@game_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Games.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
