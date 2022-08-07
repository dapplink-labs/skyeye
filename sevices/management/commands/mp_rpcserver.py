#encoding=utf-8

import grpc
from django.core.management.base import BaseCommand
from concurrent import futures
from sevices.coincorerpc import market_pb2_grpc
from sevices.grpc_server import MarketPriceServer


class Command(BaseCommand):
    def handle(self, *args, **options):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        market_pb2_grpc.add_MarketPriceServiceServicer_to_server(
            MarketPriceServer(),
            server
        )
        server.add_insecure_port('[::]:50250')
        server.start()
        server.wait_for_termination()