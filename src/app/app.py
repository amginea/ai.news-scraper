from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.jinja')

@app.route('/crawler', methods=['POST'])
def crawler():
    # Parse JSON data from the request
    data = request.get_json()
    urls = data.get('urls', [])

    if not urls:
        return jsonify({'error': 'No URLs provided.'}), 400

    # Process the URLs (example logic - print them to the console)
    print("Received URLs for processing:")
    for url in urls:
        print(url)

    # Return a success response
    return jsonify({'message': 'URLs successfully received!', 'received_urls': urls}), 200

@app.route('/search')
def search():
    return "here will be the search"

if __name__ == '__main__':
    app.run(debug=True)