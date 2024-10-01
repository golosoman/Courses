from flask import Blueprint, request, redirect, render_template
from app.bookmarks.dao.bookmarks_dao import BookmarksDAO
from app.work_with_posts.dao.posts_dao import PostsDAO
from config import BOOKMARKS_DATA_PATH, POSTS_DATA_PATH
import logging

# Создание блупринта
bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")

# Подключение логирования
logging.basicConfig(filename="logs/api.log", encoding="utf-8", level=logging.INFO)

# Подключение закладок и постов из БД
bookmarks_data = BookmarksDAO(BOOKMARKS_DATA_PATH)
posts_data = PostsDAO(POSTS_DATA_PATH)


# Функция загрузки страницы с добавлением закладки и переадресацией
@bookmarks_blueprint.route("/bookmarks/add/<int:post_id>")
def add_bookmarks_page(post_id):
    try:
        bookmarks_data.add_post_to_bookmarks(post_id)
    except ValueError as err:
        logging.info(f"/bookmarks/add/{post_id} {err}")

    return redirect("/", code=302)


# Функция загрузки страницы с удалением закладки и переадресацией
@bookmarks_blueprint.route("/bookmarks/remove/<int:post_id>")
def del_bookmarks_page(post_id):
    try:
        bookmarks_data.del_post_from_bookmarks(post_id)
    except ValueError as err:
        logging.info(f"/bookmarks/add/{post_id} {err}")

    return redirect("/", code=302)


# Функция загрузки страницы с закладками
@bookmarks_blueprint.route("/bookmarks")
def bookmarks_page():
    bookmarks = bookmarks_data.get_all_bookmarks()

    posts = posts_data.get_posts_all()

    posts_by_bookmarks = list()

    for bookmark in bookmarks:
        posts_by_bookmarks.append(posts[bookmark.get("pk") - 1])

    return render_template("bookmarks.html", posts=posts_by_bookmarks)
