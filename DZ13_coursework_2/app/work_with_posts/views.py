from flask import Blueprint, render_template, request, redirect
from app.work_with_posts.dao.posts_dao import PostsDAO
from app.work_with_posts.dao.comments_dao import CommentsDAO
from app.bookmarks.dao.bookmarks_dao import BookmarksDAO
from config import POSTS_DATA_PATH, COMMENTS_DATA_PATH, BOOKMARKS_DATA_PATH

# Создание блупринта
work_with_posts_blueprint = Blueprint("work_with_posts_blueprints", __name__, template_folder="templates")

# Загрузка постов, закладок, комментариев и БД
data_posts = PostsDAO(POSTS_DATA_PATH)
bookmarks_data = BookmarksDAO(BOOKMARKS_DATA_PATH)
data_comments = CommentsDAO(COMMENTS_DATA_PATH)


# Функция загрузки главной страницы
@work_with_posts_blueprint.route("/", methods=['GET'])
def main_page():
    user_posts = data_posts.get_posts_all()

    count_bookmarks = len(bookmarks_data.get_all_bookmarks())

    return render_template("index.html", posts=user_posts, count_bookmarks=count_bookmarks)


# Функция загрузки страницы поста по id
@work_with_posts_blueprint.route("/posts/<int:post_id>", methods=['GET'])
def post_page(post_id):
    comments_by_post_id = data_comments.get_comments_by_post_id(post_id, POSTS_DATA_PATH)

    post_by_post_id = data_posts.get_post_by_pk(post_id)

    return render_template("post.html", post=post_by_post_id,
                           comments=comments_by_post_id, count_comments=len(comments_by_post_id))


# Функция загрузки страницы поиска по ключевому слову
@work_with_posts_blueprint.route("/search", methods=['GET'])
def search_page():
    key_word = request.args.get("key_word")

    posts_by_query = data_posts.search_for_posts(key_word)

    return render_template("search.html", posts=posts_by_query, count_posts=len(posts_by_query))


# Функция загрузки страницы пользователя по го имени
@work_with_posts_blueprint.route("/users/<user_name>", methods=['GET'])
def user_page(user_name):
    posts_by_username = data_posts.get_posts_by_user(user_name)

    return render_template("user-feed.html", posts=posts_by_username, user=user_name)


# Функция загрузки страницы по названию тега в посте
@work_with_posts_blueprint.route("/tag/<tag_name>")
def tag_page(tag_name):
    posts_by_tag = data_posts.get_posts_by_tag(tag_name)

    return render_template("tag.html", posts=posts_by_tag, tag=tag_name)
