from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("APP_ENV", "dev")
    return f"""
    <h1>Senior AWS DevOps Project</h1>
    <h2>Application running on Kubernetes EKS</h2>
    <p>Environment: {env}</p>
    <p>Version: v1</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
