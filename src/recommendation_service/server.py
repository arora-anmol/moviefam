import os
from concurrent import futures
import time
from pprint import pprint
from sklearn.externals import joblib
import grpc
import recommendation_pb2
import recommendation_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MovieRecommender(recommendation_pb2_grpc.get_moviesServicer):

    def get_movies(self, request, context):
        profession = request.profession
        age = request.age
        genres = request.genres
        print(profession)
        print(age)
        print(genres)

        return recommendation_pb2.movie_response(movies=["123", "2313"] , ratings = [3, 4] )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendation_pb2_grpc.add_get_moviesServicer_to_server(MovieRecommender(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()