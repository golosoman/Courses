import logging
from datetime import datetime
from flask import Blueprint, jsonify
from app.work_with_posts.dao.posts_dao import PostsDAO
from config import POSTS_DATA_PATH


api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logs/api.log", encoding="utf-8", level=logging.INFO)

data_posts = PostsDAO(POSTS_DATA_PATH)


@api_blueprint.route("/api/posts")
def get_posts_page_json():
    posts = data_posts.get_posts_all()
    json_str = ""
    for post in posts:
        json_str += f"<p>{post}</p>"
    logging.info(f"{datetime.now()} [{logging.getLevelName(20)}]Запрос /api/posts")
    # return f"<h1>Полный список постов в виде JSON</h1>{json_str}"
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:post_id>")
def get_post_page_json_by_post_id(post_id):
    post_by_id = data_posts.get_post_by_pk(post_id)
    logging.info(f"{datetime.now()} [{logging.getLevelName(20)}]Запрос /api/posts/{post_id}")
    # return f"<h1>Один пост в виде JSON-словаря</h1><p>{post_by_id}</p>"
    return jsonify(post_by_id)
