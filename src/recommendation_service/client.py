from __future__ import print_function
import argparse
import grpc
import recommendation_pb2
import recommendation_pb2_grpc

def run(host, port):
    channel = grpc.insecure_channel('%s:%d' % (host, port))
    stub = recommendation_pb2_grpc.get_moviesStub(channel)
    request = recommendation_pb2.movie_request(
        age = 20,
        profession = "student",
        gender = 'M', 
        genres = ['comedy', 'horror']
    )
    response = stub.get_movies(request)
    print("Predicted movies are " + str(response.movies))
    print("Predicted ratings are " + str(response.ratings))

if __name__ == '__main__':
    run('localhost', 50052)

