from flask import Flask
app = Flask(__name__)

@app.route("/alerts")
def hello():
    """
    This API "endpoint" alerts user if they are in a "high crime" area
    """
    # TODO: return JSON array of recent alerts if threshold is exceeded
    return "You have no alerts!"

if __name__ == "__main__":
    app.run()
