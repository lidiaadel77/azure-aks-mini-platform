from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Azure AKS Mini Platform</h1>
    <p>This Flask app is containerized with Docker and deployed to Azure Kubernetes Service.</p>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "azure-aks-mini-platform"
    })


@app.route("/version")
def version():
    return jsonify({
        "version": os.getenv("APP_VERSION", "local-dev"),
        "environment": os.getenv("APP_ENV", "local")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
