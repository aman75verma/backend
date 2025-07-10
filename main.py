from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

app = FastAPI()
origins = ['*'] #Allow all origins (can be modified to restrict access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# input Request model
class QuestionRequest(BaseModel):
    question:str

#response body model
class AnswerResponse(BaseModel):
    answer:str

#POST endpoint
@app.post(path="/ask", response_model = AnswerResponse)
def answer_question(request:QuestionRequest):
    question = request.question
    answer = "Here is a generic answer"
    return {"answer" : answer}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

