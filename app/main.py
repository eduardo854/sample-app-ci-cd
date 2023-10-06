from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def status():
    return {"status": "ok"}


@app.get("/about")
def read_root():
    return {
        "title": "Building a GitOps structure with GitHub, Actions, DockerHub, and Helm Repository"
    }
