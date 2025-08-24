import numpy as np

from flask import Flask, request, render_template, jsonify
from services.scraper import scrape_urls
from dal.chroma import upload_from_documents
from langchain_core.documents import Document
from services.search import search_info

app = Flask(__name__)

#Home page
@app.route('/')
def index():
    return render_template('index.html.jinja')

#Crawler endpoint
@app.route('/scraper', methods=['POST'])
def scraper():
    data = request.get_json()
    urls = data.get('urls', [])

    if not urls:
        return jsonify({'error': 'No URLs provided.'}), 400
    
    upload_from_documents(scrape_urls(urls))
    return jsonify({"message":"Success"}), 200

# Search endpoint
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '')
    print(query)
    answer = search_info(query)
    return jsonify({"answer": answer}), 200

if __name__ == '__main__':
    app.run(debug=True)