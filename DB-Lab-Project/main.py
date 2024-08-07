from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, FastAPI
from fastapi.templating import Jinja2Templates
import uvicorn

from model import App

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
uri = "neo4j+s://b668c99d.databases.neo4j.io"
user = "neo4j"
password = "PVSTqrQ9e29sU01mus2qgOfOQNxFKa2fSL69EC3gsnU"
model = App(uri, user, password)

@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/add_new_student")
def add_new_student(request: Request):
    return templates.TemplateResponse("add_new_student/form.html", {"request": request})

@app.post("/add_new_student_submit")
async def add_new_student_submit(request: Request):
    data = await request.json()
    print("in insert")
    print(data)
    model.new_student(data["name"], data["score"], data["year"])
    return 0

'''
@app.get("/show_student_timetable")
def show_student_timetable(request: Request):
    return templates.TemplateResponse("show_student_timetable/form.html", {"request": request})

@app.get("/show_student_timetable_submit/{name}")
def show_student_timetable_submit(request: Request, name):
    print("search for student with name {}".format(name))
    student_timetable = ["11pm to 00am tokhmemorgh begiram?", "2am to 3am shamemoon nashe aroosak?"]
    return templates.TemplateResponse("show_student_timetable/result.html", {"request": request, "timetable":student_timetable})
'''

@app.get("/find_student_score")
def find_student_score(request: Request):
    return templates.TemplateResponse("find_student_score/form.html", {"request": request})

@app.get("/find_student_score_submit/{name}")
def find_student_score_submit(request: Request, name):
    score = model.find_student_score(name)
    return templates.TemplateResponse("find_student_score/result.html", {"request": request, "score":score})

@app.get("/delete_student")
def delete_student(request: Request):
    return templates.TemplateResponse("delete_student/form.html", {"request": request, "status": "beforedelete"})

@app.get("/delete_student_submit/{name}")
def delete_student_submit(request: Request, name):
    model.delete_student(name)
    return templates.TemplateResponse("delete_student/form.html", {"request": request, "status": "afterdelete"})


@app.get("/update_student_score")
def update_student_score(request: Request):
    return templates.TemplateResponse("update_student_score/form.html", {"request": request, "status": "beforedelete"})

@app.get("/update_student_score_submit/{name}/{score}")
def update_student_score_submit(request: Request, name, score):
    model.update_student_score(name, score)
    return templates.TemplateResponse("update_student_score/form.html", {"request": request, "status": "afterdelete"})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)