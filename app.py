from flask import Flask, send_from_directory
import show_picture.main as main
import picture_loader.loader as loader


app = Flask(__name__)

app.register_blueprint(main.show_picture_blueprint, url_prefix='/')
app.register_blueprint(loader.picture_loader_blueprint, url_prefix='/post/')

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

@app.route('/uploads/images/<path:path>')
def static_dir(path):
    return send_from_directory("uploads/images", path)


@app.errorhandler(413)
def page_not_found(e):
    return "<h1>Файл большеват</h1><p>Поищите поменьше!</p>", 413

app.run()
