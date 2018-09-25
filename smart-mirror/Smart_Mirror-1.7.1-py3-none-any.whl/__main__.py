# import smart_mirror.app
# from smart_mirror import app
from smart_mirror.app import app, socketio
# from pyfladesk import init_gui


def main():
    # app.run()
    socketio.run(app, host='0.0.0.0', log_output=False)
    # init_gui(app)

if __name__ == "__main__":
    main()