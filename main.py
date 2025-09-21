from flask import Flask, render_template
import redis

app = Flask(__name__)


redis_conn = redis.StrictRedis(host="redis", port=6379, decode_responses=True)
PAGE_COUNTER_KEY = "page_counter"

@app.route("/")
def index():
    count = redis_conn.incr(PAGE_COUNTER_KEY)
    return render_template("index.html", page_count=count)

if __name__ == "__main__":    
    app.run(debug=True, host="0.0.0.0", port=5000)

