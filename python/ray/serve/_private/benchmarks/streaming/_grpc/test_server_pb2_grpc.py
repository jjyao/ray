# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ray.serve._private.benchmarks.streaming._grpc import (
    test_server_pb2 as backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2,
)


class GRPCTestServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Unary = channel.unary_unary(
            "/GRPCTestServer/Unary",
            request_serializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.SerializeToString,
            response_deserializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.FromString,
        )
        self.ClientStreaming = channel.stream_unary(
            "/GRPCTestServer/ClientStreaming",
            request_serializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.SerializeToString,
            response_deserializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.FromString,
        )
        self.ServerStreaming = channel.unary_stream(
            "/GRPCTestServer/ServerStreaming",
            request_serializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.SerializeToString,
            response_deserializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.FromString,
        )
        self.BidiStreaming = channel.stream_stream(
            "/GRPCTestServer/BidiStreaming",
            request_serializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.SerializeToString,
            response_deserializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.FromString,
        )


class GRPCTestServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Unary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ClientStreaming(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ServerStreaming(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BidiStreaming(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_GRPCTestServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Unary": grpc.unary_unary_rpc_method_handler(
            servicer.Unary,
            request_deserializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.FromString,
            response_serializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.SerializeToString,
        ),
        "ClientStreaming": grpc.stream_unary_rpc_method_handler(
            servicer.ClientStreaming,
            request_deserializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.FromString,
            response_serializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.SerializeToString,
        ),
        "ServerStreaming": grpc.unary_stream_rpc_method_handler(
            servicer.ServerStreaming,
            request_deserializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.FromString,
            response_serializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.SerializeToString,
        ),
        "BidiStreaming": grpc.stream_stream_rpc_method_handler(
            servicer.BidiStreaming,
            request_deserializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.FromString,
            response_serializer=backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "GRPCTestServer", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class GRPCTestServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Unary(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/GRPCTestServer/Unary",
            backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.SerializeToString,
            backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ClientStreaming(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            "/GRPCTestServer/ClientStreaming",
            backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.SerializeToString,
            backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ServerStreaming(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/GRPCTestServer/ServerStreaming",
            backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.SerializeToString,
            backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BidiStreaming(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            "/GRPCTestServer/BidiStreaming",
            backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Request.SerializeToString,
            backend_dot_server_dot_common_dot_clients_dot_grpc_dot_proto_dot_test__server__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
