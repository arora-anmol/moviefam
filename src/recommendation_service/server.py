import os
from concurrent import futures
import time
from pprint import pprint
from sklearn.externals import joblib
import grpc
import recommendation_pb2
import recommendation_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MovieRecommender(get_moviesServicer):
    _model = None

    @classmethod
    def get_or_create_model(cls):
        """
        Get KMeans model from file
        """
        if cls._model is None:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model', 'user_model.pickle')
            cls._model = joblib.load(path)
        return cls._model

    def PredictIrisSpecies(self, request, context):
            model = self.__class__.get_or_create_model()
            sepal_length = request.sepal_length
            sepal_width = request.sepal_width
            petal_length = request.petal_length
            petal_width = request.petal_width
            result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]]) # need to change this function
            return recommendation_pb2.movei_response(species=result[0])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iris_pb2_grpc.add_get_moviesServicer_to_server(MovieRecommender(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()