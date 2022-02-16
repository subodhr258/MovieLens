from flask import Flask, request, jsonify
import pickle
import numpy as np
from model import ContentBased, CollabBased, HybridBased, ModelBased

app = Flask(__name__)

# the recommender module
class Recommender:

    def __init__(self):
        with open('./Files/model_svd.pkl', 'rb') as f:
            self.algo = pickle.load(f)
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
        self.clf_algo = ModelBased(self.algo)

    # def parsing_args(self):
    #     self.parser = reqparse.RequestParser()
    #     self.parser.add_argument('movie', required=False,
    #                              help="movie title followed by year")
    #     self.parser.add_argument('limit', required=False,
    #                              help="N in top N films")

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

    def get_user_recommendation(self, userId, n):
        if userId in self.rating.userId.unique():
            ui_list = self.rating[
                self.rating.userId == userId].movieId.tolist()
            d = {k: v for k, v in self.movie_map.items() if v not in ui_list}
            output = self.clf_algo.predict_top_n_user(userId, d, n)
        else:
            output = None
        return output

# the app


ex = Recommender()
@app.route('/movies/<basis>/',methods=['GET'])
# class MovieBasis(Resource):
def getMovieBasis(basis):
    movie = request.args.get("movie",None)
    n = request.args.get("limit",None)
    output = ex.get_all_recommendations(movie, int(n))
    return jsonify(output[basis])

# @app.route('/users/<userId>/',methods=['GET'])
# # class UserBasis(Resource):
# def getUserBasis(userId):
#     n = request.args.get("limit",None)
#     output = ex.get_user_recommendation(int(userId), int(n))
#     return jsonify(output)

app.run(debug=True, port=8000)