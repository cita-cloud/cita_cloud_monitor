# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import blockchain_pb2 as blockchain__pb2
import common_pb2 as common__pb2
import executor_pb2 as executor__pb2


class ExecutorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Exec = channel.unary_unary(
                '/executor.ExecutorService/Exec',
                request_serializer=blockchain__pb2.CompactBlock.SerializeToString,
                response_deserializer=common__pb2.Hash.FromString,
                )
        self.Call = channel.unary_unary(
                '/executor.ExecutorService/Call',
                request_serializer=executor__pb2.CallRequest.SerializeToString,
                response_deserializer=executor__pb2.CallResponse.FromString,
                )


class ExecutorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Exec(self, request, context):
        """exec a block return executed_block_hash
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExecutorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Exec': grpc.unary_unary_rpc_method_handler(
                    servicer.Exec,
                    request_deserializer=blockchain__pb2.CompactBlock.FromString,
                    response_serializer=common__pb2.Hash.SerializeToString,
            ),
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=executor__pb2.CallRequest.FromString,
                    response_serializer=executor__pb2.CallResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'executor.ExecutorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExecutorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Exec(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/executor.ExecutorService/Exec',
            blockchain__pb2.CompactBlock.SerializeToString,
            common__pb2.Hash.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/executor.ExecutorService/Call',
            executor__pb2.CallRequest.SerializeToString,
            executor__pb2.CallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)