from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
app = Flask(__name__)
REQUEST_COUNT = Counter(
    "library_app_requests_total",
    "Total number pf requests to the library application",
    ["endpoint"]
)
@app.route("/")
def home():
    REQUEST_COUNT.labels(endpoint="/").inc()
    return "Library Management System"
@app.route("/books")
def books():
    REQUEST_COUNT.labels(endpoint="/books").inc()
    return "List of Books"
@app.route("/members")
def members():
    REQUEST_COUNT.labels(endpoint="/members").inc()
    return "Library Members"
@app.route("/about")
def about():
    REQUEST_COUNT.labels(endpoint="/about").inc()
    return "About the Library"
@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        content_type=CONTENT_TYPE_LATEST
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)