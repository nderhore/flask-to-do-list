import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Configuration de la base de données
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False