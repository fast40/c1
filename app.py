from flask import Flask, request, render_template, jsonify
from create_datasets import DATABASE
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('mongodb://localhost:27017/qualtricks')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_responses')
def get_responses():
    try:
        question_number = int(request.args.get('question_number'))
    except Exception:
        return jsonify({})

    responses = list(client[DATABASE]['responses'].aggregate([{'$sample': {'size': 4}}]))

    response_set = {
        'response_numbers': ' '.join(response['response_number'] for response in responses),
        'initial_answers': [response['initial_answers'][question_number - 1] for response in responses],
        'meta_errors': [response['meta_errors'][question_number - 1] for response in responses],
    }

    return jsonify(response_set)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
