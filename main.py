from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from lxml import etree
import uvicorn

app = FastAPI()


@app.post("/consume-xml")
async def consume_xml(request: Request):
    try:
        xml_bytes = await request.body()
        # Parse the XML data
        root = etree.fromstring(xml_bytes)

        # Example: Extracting some data from the XML
        extracted_data = {}
        for element in root.iter():
            extracted_data[element.tag] = element.text

        # Return the extracted data as JSON response
        return JSONResponse(content=extracted_data)

    except etree.XMLSyntaxError as e:
        raise HTTPException(status_code=400, detail="Invalid XML data")


@app.get("/")
async def read_root():
    return {"message": "Welcome to the XML consuming API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
