from flask import Flask
from flask import jsonify
import Instagram
import random as rd

app = Flask(__name__)

@app.route("/instagram")
def getInstaMeme():
    posts = Instagram.InstagramCrawler()
    postsDetails = posts.results
    postsDetail: dict = postsDetails[0]
    memes = []
    for _ in postsDetail.values():
        memes.extend(_)

    meme = memes[rd.randint(0, len(memes)-1)]
    return jsonify(meme)

@app.route("/reddit")
def getHello():
    return jsonify({"hello": "world"})

@app.errorhandler(404)
@app.route('/<lol>')
def not_found(lol):
    return "<h1>Oops, I guess You are Lost?</h1>"


if __name__ == '__main__':
    app.run()
