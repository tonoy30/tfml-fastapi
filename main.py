from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse

from models.serve_model import predict, read_imagefile

api_desc = """
    <p>Author: Md. Tonoy Akando</p>
    <p>Email: tonoy.sust@gmail.com</p>
"""
app = FastAPI(title="Tensorflow and Fastapi", description=api_desc)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)

    return prediction
