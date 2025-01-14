from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['github_webhooks']
collection = db['events']

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    action = data.get('action')
    repo = data.get('repository')
    actor = data.get('actor')
    timestamp = data.get('timestamp')

    if action == 'push':
        ref = data.get('ref').split('/')[-1]
        collection.insert_one({
            'type': 'push',
            'author': actor,
            'to_branch': ref,
            'timestamp': timestamp
        })
    elif action == 'pull_request':
        from_branch = data.get('pull_request', {}).get('head', {}).get('ref')
        to_branch = data.get('pull_request', {}).get('base', {}).get('ref')
        collection.insert_one({
            'type': 'pull_request',
            'author': actor,
            'from_branch': from_branch,
            'to_branch': to_branch,
            'timestamp': timestamp
        })
    elif action == 'merged':
        from_branch = data.get('pull_request', {}).get('head', {}).get('ref')
        to_branch = data.get('pull_request', {}).get('base', {}).get('ref')
        collection.insert_one({
            'type': 'merge',
            'author': actor,
            'from_branch': from_branch,
            'to_branch': to_branch,
            'timestamp': timestamp
        })
    @app.route('/events', methods=['GET'])
    def get_events():
    events = list(collection.find({}, {'_id': 0}))  # Exclude the MongoDB ID
    return jsonify(events), 200

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5000)
