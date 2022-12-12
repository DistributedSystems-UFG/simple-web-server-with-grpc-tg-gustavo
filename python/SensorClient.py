from __future__ import print_function
import logging

import grpc
import SensorService_pb2
import SensorService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = SensorService_pb2_grpc.SensorServiceStub(channel)

        # Registra dados do sensor
        response = stub.RegistrarDadoSensor(SensorService_pb2.SensorData(id=4, data='12/12/2022', localizacao='Sala-102', temperatura=22.0))
        print ('Dados do Sensor registado' + response.status)

        # Consulta dados por data
        response = stub.ConsultarDadosSensoresPorData(SensorService_pb2.Data(data='11/12/2022'))
        print ('Dados do Sensor consultado: ' + str(response))

        # Consulta dados por localização
        response = stub.ConsultarDadosSensoresPorLocalizacao(SensorService_pb2.Localizacao(localizacao='Sala-102'))
        print ('Dados do Sensor consultado: ' + str(response))


if __name__ == '__main__':
    logging.basicConfig()
    run()