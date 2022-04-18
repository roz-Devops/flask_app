from flask import Flask
from flask import request, Response
from flask_healthz import healthz
from flask_healthz import HealthError
from prometheus_flask_exporter import PrometheusMetrics
import sys

app = Flask(__name__)
port = sys.argv[1];
app.register_blueprint(healthz, url_prefix="/healthz")
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='flask_app_ubuntu:latest')


def printok():
    print("It's Alive and Works smoothly!")

def liveness():
    try:
        printok()
    except Exception:
        raise HealthError(" Liveness Failure!")

def readiness():
    try:
        printok()
    except Exception:
        raise HealthError("Readiness Failure, Can't serve Traffic!")

app.config.update(
    HEALTHZ = {
        "live": app.name + ".liveness",
        "ready": app .name+ ".readiness",
    }
)


@app.route("/")
def home():
    msg = request.args.get('msg')
    return Response(msg, 200)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=int(port))
