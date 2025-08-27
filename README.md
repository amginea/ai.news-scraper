# ai.news-scraper

## Description
It is the small web service with ui part developed by using Python and Flask. Implements the web page scraping and semantic search on the content retrieved from pages

## Dependencies
- python
- flask
- pip
- venv
- langchain
- langchain_community
- chromadb
- firecrawl

## How to run locally
1. Install [python](https://www.python.org/downloads/)
2. Configure virtual environment by usng `venv`. Run the following code being in root directory of the repo
```bash
py python3 -m venv .venv
```
3. Activate virtual environment to install all packages near to repo
```bash
.venv/Scripts/activate
```
You should see the (.venv) on the left side, see the following:

<img width="347" height="23" alt="image" src="https://github.com/user-attachments/assets/886ea093-d72c-4dd2-baaf-abfc19d60259" />

4. Install and update `pip` by using the following cmd
```bash
py -m pip install --upgrade pip
py -m pip --version
```

5. Install the following packages
```bash
pip install chromadb
pip install langchain
pip install langchain_community
pip install flask
pip install firecrawl-py
```
6. Run chromadb server by the following script (use different terminal). Virtual environment should be activated. See above
```bash
.\scripts\start_chroma_server.bat
```

7. Run web application script (use different terminal). Virtual environment should be activated. See above
```bash
python ./src/app.py
```

8. Reference to host in browser
```bash
http://127.0.0.1:5000/
```

