from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json
from pos_tagger import POSTagger
from hmm_model import HiddenMarkovModel

app = Flask(__name__)
api = Api(app)

hmm = HiddenMarkovModel()
with open("data/tagged_sentences.json", "r") as f:
    tagged_sentences = json.load(f)

hmm.train(tagged_sentences)
pos_tagger = POSTagger(hmm)
class POSTagging(Resource):
    def post(self):
        try:
            data = request.get_json()
            sentence = data.get("sentence", [])
            
            if not sentence or not isinstance(sentence, list):
                return {"error": "Invalid input. Please provide a list of words."}, 400

            tags = pos_tagger.tag_sentence(sentence)
            return {"sentence": sentence, "tags": tags}, 200
        except Exception as e:
            return {"error": str(e)}, 500

api.add_resource(POSTagging, "/tag")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
