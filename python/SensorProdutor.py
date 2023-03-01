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
        response = stub.RegistrarDadoSensor(SensorService_pb2.DadoSensor(id=4, data='11/12/2022', localizacao='Sala-102', temperatura=16.0))
        print ('Cadastro de dado sensor 1:' + response.status)

        response = stub.RegistrarDadoSensor(SensorService_pb2.DadoSensor(id=5, data='12/12/2022', localizacao='Sala-101', temperatura=26.6))
        print ('Cadastro de dado sensor 2:' + response.status)

        response = stub.RegistrarDadoSensor(SensorService_pb2.DadoSensor(id=6, data='12/12/2022', localizacao='Sala-102', temperatura=30.2))
        print ('Cadastro de dado sensor 3:' + response.status)


if __name__ == '__main__':
    logging.basicConfig()
    run()