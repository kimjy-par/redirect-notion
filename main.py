from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

@app.get("/")
def redirect_notion():
    return RedirectResponse("https://freckle-moonstone-72f.notion.site/tutorial-bb0a5eb7c04549588d78ed32d8a2cfd7?pvs=4")
