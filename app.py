from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import uvicorn
from dotenv import load_dotenv
from QA_System.retrieval_generation import get_result

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get_answer")
async def get_answer(request: Request, question: str = Form(...)):
    answer = get_result(question)
    
    if not answer:
        answer = "Sorry, I couldn't process your question. Please try again."
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "question": question,
        "answer": answer
    })

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)