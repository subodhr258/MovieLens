from flask import Flask, request, jsonify
import pickle
import numpy as np
from model import ContentBased, CollabBased, HybridBased
import os

app = Flask(__name__)

# the recommender module
class Recommender:

    def __init__(self):
        with open('./Files/map.pkl', 'rb') as f:
            self.movie_map = pickle.load(f)
        with open('./Files/rating.pkl', 'rb') as f:
            self.rating = pickle.load(f)
        with open('./Files/latent_collaborative.pkl', 'rb') as f:
            latent_collab = pickle.load(f)
        with open('./Files/latent_content.pkl', 'rb') as f:
            latent_content = pickle.load(f)

        self.clf_content = ContentBased(latent_content)
        self.clf_collab = CollabBased(latent_collab)
        self.clf_hybrid = HybridBased(latent_content, latent_collab)

    def get_all_recommendations(self, moviename, n):
        if moviename in self.movie_map.keys():
            output = {
                'content': {'content':
                            self.clf_content.predict_top_n(moviename, n)},
                'collaborative': {'collaborative':
                                  self.clf_collab.predict_top_n(moviename, n)},
                'hybrid': {'hybrid':
                           self.clf_hybrid.predict_top_n(moviename, n)},
                     }
        else:
            output = None
        return output

ex = Recommender()
@app.route('/movies/<basis>/',methods=['GET'])
def getMovieBasis(basis):
    movie = request.args.get("movie",None)
    n = request.args.get("limit",None)
    output = ex.get_all_recommendations(movie, int(n))
    return jsonify(output[basis])

if __name__=='__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(debug=True, port=port)