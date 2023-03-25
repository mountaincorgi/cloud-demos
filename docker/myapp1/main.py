from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return "Hello world!"


@app.get("/health")
def health():
    return "OK!"


# Allows running as a module, and importing
# Can also run from the Dockerfile using "python -m main.py"
if __name__ == "__main__":
    # Do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)
