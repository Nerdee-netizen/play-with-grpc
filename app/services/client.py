import grpc
import sum_pb2
import sum_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = sum_pb2_grpc.SumServiceStub(channel)
        response = stub.Sum(sum_pb2.SumRequest(num1=3, num2=5))
        print(f"Sum of 3 and 5 is: {response.result}")

if __name__ == '__main__':
    run()
