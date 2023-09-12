# """Models for Playlist app."""
# from flask import Flask

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# # def connect_db(app):
# #     """Connect this database to provided Flask app.
    
# #     You should call this in your Flask app.
# #     """

# #     db.app = app
# #     db.init_app(app)




# class Playlist(db.Model):
#     """Playlist."""

#     # ADD THE NECESSARY CODE HERE
#     __tablename__ = "playlists"

#     id = db.Column(db.Integer, 
#                    primary_key = True, 
#                    autoincrement = True
#     )
#     name = db.Column(db.Text, nullable=False)

#     description = db.Column(db.Text)

#     songs = db.relationship('Song', secondary='playlists_songs', backref='playlists')


# class Song(db.Model):
#     """Song."""

#     # ADD THE NECESSARY CODE HERE
#     __tablename__ = "songs"

#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)

#     title = db.Column(db.Text, nullable=False)

#     artist = db.Column(db.Text, nullable=False)


# class PlaylistSong(db.Model):
#     """Mapping of a playlist to a song."""

#     # ADD THE NECESSARY CODE HERE
#     __tablename__ = "playlist_songs"

#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)

#     playlist_id = db.Column(db.Integer, db.ForeignKey(Playlist.id), nullable = False)

#     song_id = db.Column(db.Integer, db.ForeignKey(Song.id), nullable = True)


# # DO NOT MODIFY THIS FUNCTION
# def connect_db(app):
#     """Connect to database."""

#     db.app = app
#     db.init_app(app)

"""Models for Playlist app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    songs = db.relationship('Song', secondary='playlist_songs', backref='playlists')

class Song(db.Model):
    """Song."""
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "playlist_songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey(Playlist.id), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey(Song.id), nullable=False)

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)
