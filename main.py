import responder
import requests
from loguru import logger

api = responder.API()

@api.route("/text")
def text(req, resp):
    logger.debug("return text")
    resp.text = "text"


@api.route("/post")
def post(req, resp):
    logger.debug("post")
    r = requests.post("https://www.strava.com/oauth/token", {"payload": "payload"})
    resp.text = r.text


if __name__ == "__main__":
    api.run()