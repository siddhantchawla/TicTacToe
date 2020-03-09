from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp
import time


from game import moves,gameOver,tictactoe

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
        session["score"] = {"X":0,"O":0,"Draw":0}

    if session["turn"] == "O":
    # Comment out to make computer play automatically
    	# time.sleep(2)
    	value,r,c = tictactoe(session["board"],session["turn"])
    	return redirect(url_for("play",row = r,col = c))

    return render_template("game.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
	# print("hii")
	session["board"][row][col] = session["turn"]


	if gameOver(session["turn"],session["board"]):
		session["score"][session["turn"]] += 1
		return render_template("gameOver.html",game=session["board"],winner=session["turn"],score_x = session["score"]["X"],score_o = session["score"]["O"],score_draw = session["score"]["Draw"])

	if len(moves(session["board"])) == 0:
		session["score"]["Draw"] += 1
		return render_template("gameOver.html",game=session["board"],winner="Draw",score_x = session["score"]["X"],score_o = session["score"]["O"],score_draw = session["score"]["Draw"])

	if(session["turn"] == "X"):
		session["turn"] = "O"
	else:
		session["turn"] = "X"
	
	return redirect(url_for("index"))

@app.route("/reset")
def reset():
	session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
	session["turn"] = "X"
	return redirect(url_for("index"))


@app.route("/playAI")
def playAI():
	value,row,col = tictactoe(session["board"],session["turn"])
	return redirect(url_for("play",row = row,col = col))










