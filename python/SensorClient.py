from __future__ import print_function
import logging

import grpc
import SensorService_pb2
import SensorService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = SensorService_pb2_grpc.SensorServiceStub(channel)
        try:
            # Consulta dados por data
            response = stub.ConsultarDadosSensoresPorData(SensorService_pb2.Data(data='12/12/2022'))
            print("Consulta realizada para data 12/12/2022 \n")
            for item in response.dados_sensor:
                print('ID: {}'.format(item.id))
                print('Data: {}'.format(item.data))
                print('Localização: {}'.format(item.localizacao))
                print('Temperatura: {}'.format(item.temperatura))
            print("\n\n")
            # Consulta dados por localização
            response = stub.ConsultarDadosSensoresPorLocalizacao(SensorService_pb2.Localizacao(localizacao='Sala-102'))
            print("Consulta realizada para localização: Sala-102 \n")
            for item in response.dados_sensor:
                print('ID: {}'.format(item.id))
                print('Data: {}'.format(item.data))
                print('Localização: {}'.format(item.localizacao))
                print('Temperatura: {}'.format(item.temperatura))
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAUTHENTICATED:
                print('Erro na requisicao.\n')


if __name__ == '__main__':
    logging.basicConfig()
    run()