# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import common_pb2 as common__pb2
import storage_pb2 as storage__pb2


class StorageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Store = channel.unary_unary(
                '/storage.StorageService/Store',
                request_serializer=storage__pb2.Content.SerializeToString,
                response_deserializer=common__pb2.StatusCode.FromString,
                )
        self.Load = channel.unary_unary(
                '/storage.StorageService/Load',
                request_serializer=storage__pb2.ExtKey.SerializeToString,
                response_deserializer=storage__pb2.Value.FromString,
                )
        self.Delete = channel.unary_unary(
                '/storage.StorageService/Delete',
                request_serializer=storage__pb2.ExtKey.SerializeToString,
                response_deserializer=common__pb2.StatusCode.FromString,
                )


class StorageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Store(self, request, context):
        """store key/value
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Load(self, request, context):
        """given a ext key return value
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """given a ext key delete it
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StorageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Store': grpc.unary_unary_rpc_method_handler(
                    servicer.Store,
                    request_deserializer=storage__pb2.Content.FromString,
                    response_serializer=common__pb2.StatusCode.SerializeToString,
            ),
            'Load': grpc.unary_unary_rpc_method_handler(
                    servicer.Load,
                    request_deserializer=storage__pb2.ExtKey.FromString,
                    response_serializer=storage__pb2.Value.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=storage__pb2.ExtKey.FromString,
                    response_serializer=common__pb2.StatusCode.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'storage.StorageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StorageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Store(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/storage.StorageService/Store',
            storage__pb2.Content.SerializeToString,
            common__pb2.StatusCode.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Load(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/storage.StorageService/Load',
            storage__pb2.ExtKey.SerializeToString,
            storage__pb2.Value.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/storage.StorageService/Delete',
            storage__pb2.ExtKey.SerializeToString,
            common__pb2.StatusCode.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
