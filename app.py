# from flask import Flask, redirect, render_template, flash  # Added flash import
# from flask_debugtoolbar import DebugToolbarExtension

# from models import db, connect_db, Playlist, Song, PlaylistSong
# from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

# app = Flask(__name__)
# app.app_context().push()
# # ... [rest of the configuration and setup]
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///playlist"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SECRET_KEY'] = 'secret'
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)

# connect_db(app)

# @app.route("/")
# def root():
#     """Homepage: redirect to /playlists."""

#     return redirect("/playlists")



# @app.route("/playlists/<int:playlist_id>")
# def show_playlist(playlist_id):
#     """Show detail on specific playlist."""
#     playlist = Playlist.query.get_or_404(playlist_id)
#     return render_template("playlist.html", playlist=playlist)

# # ... [rest of the routes]

# @app.route("/songs/<int:song_id>")
# def show_song(song_id: int):
#     """return a specific song"""
#     song = Song.query.get_or_404(song_id)  # Fixed typo here
#     return render_template("song.html", song=song)

# # ... [rest of the routes]

# @app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
# def add_song_to_playlist(playlist_id):
#     """Add a playlist and redirect to list."""
#     playlist = Playlist.query.get_or_404(playlist_id)
#     form = NewSongForPlaylistForm()

#     curr_on_playlist = [song.id for song in playlist.songs]
#     form.song.choices = [
#         (song.id, song.title) for song in Song.query.filter(
#             Song.id.notin_(curr_on_playlist)  # Fixed typo here
#         ).all()
#     ]

#     # ... [rest of the code]

#     if form.validate_on_submit():
#         playlist_song = PlaylistSong(song_id=form.song.data, playlist_id=playlist_id)  # Fixed typo here

#         db.session.add(playlist_song)
#         db.session.commit()

#         return redirect(f"/playlists/{playlist_id}")

#     return render_template("add_song_to_playlist.html",
#                              playlist=playlist,
#                              form=form)
from flask import Flask, redirect, render_template, flash  # Added flash import
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.app_context().push()
# ... [rest of the configuration and setup]
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///playlist"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def root():
    """Homepage: redirect to /playlists."""
    return redirect("/playlists")

@app.route("/playlists")
def show_playlists():
    """Show all playlists."""
    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)

@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    return render_template("playlist.html", playlist=playlist)

# ... [rest of the routes]

@app.route("/songs/<int:song_id>")
def show_song(song_id: int):
    """Return a specific song."""
    song = Song.query.get_or_404(song_id)
    return render_template("song.html", song=song)

# ... [rest of the routes]

@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""
    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    curr_on_playlist = [song.id for song in playlist.songs]
    form.song.choices = [
        (song.id, song.title) for song in Song.query.filter(
            Song.id.notin_(curr_on_playlist)
        ).all()
    ]

    # ... [rest of the code]

    if form.validate_on_submit():
        playlist_song = PlaylistSong(song_id=form.song.data, playlist_id=playlist_id)

        db.session.add(playlist_song)
        db.session.commit()

        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html", playlist=playlist, form=form)
