import os
import flask

def create_app():
    '''
    Function: create_app
    Summary: Создание flask приложения
    '''

    app = flask.Flask(__name__,
                      instance_relative_config=True,
                      template_folder="templates",
                      static_folder="static")

    # загружаем настройки
    app.config.from_pyfile('config.py', silent=False)

    # Главная страница сайта
    @app.route('/')
    @app.route('/index.html')
    def index_page():
        return flask.render_template('index.html')

    return app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    create_app().run()