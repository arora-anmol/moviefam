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
    _model = None
    _movies_data = None

    @classmethod
    def get_or_create_model(cls):
        """
        Get or create clustering model
        """
        if cls._model is None:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model', 'clustering.pickle')
            cls._model = joblib.load(path)
        return cls._model

    @classmethod
    def in_memory_cluster_data(cls):
        if _movies_data is None:
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model', 'movies_data.json')
            cls._movies_data = json.loads(file_path)


    def get_movies(self, request, context):
        self.__class__.in_memory_cluster_data()
        self.profession = request.profession
        self.age = request.age
        self.genres = request.genres
        self.gender = request.gender
        print(self.profession)
        print(self.age)
        print(self.genres)
        print(self.gender)

        results = self.__get_recommendations()
        return recommendation_pb2.movie_response(movies=results['movies'], ratings = results['ratings'])
    
    def __get_recommendations(self):
        clustering_model = self.__class__.get_or_create_model()
        user_vector = self.create_user_vector()
        user_cluster = clustering_model.predict(user_vector) # need to add stuff here

        top_movies = []
    



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