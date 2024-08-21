import os
from flask import Flask
from application.database import db
from application.config import LocalDevlopmentConfig
from application import config
app=None

def create_app():
    app=Flask(__name__,template_folder="templates")
    if os.getenv("ENV","devlopment")=="production":
        raise Exception("Currently working on it...")
    else:
        print("gfds")
        app.config.from_object(LocalDevlopmentConfig)
        db.init_app(app)
        app.app_context().push()
        return app

app=create_app()

from application.controlers import *
 
if __name__=="__main__":
    app.debug=True
    app.run()