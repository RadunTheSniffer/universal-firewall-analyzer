from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja templates directory
templates = Jinja2Templates(directory="templates")

# Example endpoint that renders a Jinja template
@app.get("/dashboard/")
def render_dashboard(request: Request):
    tasks = [
        {"name": "Task 1", "time_taken": 3.5, "difficulty": 2},
        {"name": "Task 2", "time_taken": 5.0, "difficulty": 4},
    ]
    return templates.TemplateResponse("dashboard.html", {"request": request, "tasks": tasks})


