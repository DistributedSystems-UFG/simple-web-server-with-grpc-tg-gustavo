# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import SensorService_pb2 as SensorService__pb2


class SensorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegistrarDadoSensor = channel.unary_unary(
                '/sensor_service.SensorService/RegistrarDadoSensor',
                request_serializer=SensorService__pb2.DadoSensor.SerializeToString,
                response_deserializer=SensorService__pb2.StatusReply.FromString,
                )
        self.ConsultarDadosSensoresPorData = channel.unary_unary(
                '/sensor_service.SensorService/ConsultarDadosSensoresPorData',
                request_serializer=SensorService__pb2.Data.SerializeToString,
                response_deserializer=SensorService__pb2.ListaDadosSensores.FromString,
                )
        self.ConsultarDadosSensoresPorLocalizacao = channel.unary_unary(
                '/sensor_service.SensorService/ConsultarDadosSensoresPorLocalizacao',
                request_serializer=SensorService__pb2.Localizacao.SerializeToString,
                response_deserializer=SensorService__pb2.ListaDadosSensores.FromString,
                )


class SensorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegistrarDadoSensor(self, request, context):
        """Registra o dado de um sensor
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsultarDadosSensoresPorData(self, request, context):
        """Consulta os dados de um sensor pela data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsultarDadosSensoresPorLocalizacao(self, request, context):
        """Consulta os dados de um sensor pela localização
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SensorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegistrarDadoSensor': grpc.unary_unary_rpc_method_handler(
                    servicer.RegistrarDadoSensor,
                    request_deserializer=SensorService__pb2.DadoSensor.FromString,
                    response_serializer=SensorService__pb2.StatusReply.SerializeToString,
            ),
            'ConsultarDadosSensoresPorData': grpc.unary_unary_rpc_method_handler(
                    servicer.ConsultarDadosSensoresPorData,
                    request_deserializer=SensorService__pb2.Data.FromString,
                    response_serializer=SensorService__pb2.ListaDadosSensores.SerializeToString,
            ),
            'ConsultarDadosSensoresPorLocalizacao': grpc.unary_unary_rpc_method_handler(
                    servicer.ConsultarDadosSensoresPorLocalizacao,
                    request_deserializer=SensorService__pb2.Localizacao.FromString,
                    response_serializer=SensorService__pb2.ListaDadosSensores.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sensor_service.SensorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SensorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegistrarDadoSensor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_service.SensorService/RegistrarDadoSensor',
            SensorService__pb2.DadoSensor.SerializeToString,
            SensorService__pb2.StatusReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConsultarDadosSensoresPorData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_service.SensorService/ConsultarDadosSensoresPorData',
            SensorService__pb2.Data.SerializeToString,
            SensorService__pb2.ListaDadosSensores.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConsultarDadosSensoresPorLocalizacao(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_service.SensorService/ConsultarDadosSensoresPorLocalizacao',
            SensorService__pb2.Localizacao.SerializeToString,
            SensorService__pb2.ListaDadosSensores.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
