# KR2: Kolomoets
import os

import redis
from flask import Flask, request

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)


@app.route("/")
def index():
    hits = r.incr("hits")
    return (
        f"KR2 | {os.getenv('STUDENT', 'unknown')} | "
        f"container{os.uname().nodename} | hits: {hits}\n"
    )


@app.route("/health")
def health():
    return "ok\n"


@app.route("/whoami")
def whoami():
    return "\n".join([
        f"scheme: {request.headers.get('X-Forwarded-Proto', 'none')}",
        f"client: {request.headers.get('X-Real-IP', 'none')}",
        f"host: {request.headers.get('Host', 'none')}",
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
