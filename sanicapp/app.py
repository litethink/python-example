from sanic import Sanic


test_config = {
    "appname" : "test",
    "mysql" : {
        "host"  : "127.0.0.1",
        "db"    : "retail001",
        "user"    : "retail001",
        "password"    : "001retail"
        }
    }
class App:
    app = Sanic(test_config.get("appname"))
    @staticmethod
    def run(cls):
        cls.app.run()

