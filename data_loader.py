import os
import requests
from dotenv import load_dotenv
from langchain_community.document_loaders import JSONLoader
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.documents import Document

load_dotenv()

DATA_API = os.getenv("DINESPHERE_DATA_API")

data = requests.get(DATA_API).json()
docs = []

for item in data:
    docs.append(
        Document(
            page_content=str(item),
            metadata={"source": "api"}
        )
    )

loader = JSONLoader(
    file_path=docs,
    jq_schema=".orders[]"
)

data = loader.load()
print(data)