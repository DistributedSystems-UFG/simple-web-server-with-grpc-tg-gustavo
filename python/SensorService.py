from concurrent import futures
import logging

import grpc
import SensorService_pb2
import SensorService_pb2_grpc

tempDB=[
 {
 'id':1,
 'data':'10/12/2022',
 'localizacao':'Sala-101',
 'temperatura':22.5
 },
{
 'id':2,
 'data':'11/12/2022',
 'localizacao':'Sala-102',
 'temperatura':24.5
 },
 {
 'id':1,
 'data':'11/12/2022',
 'localizacao':'Sala-101',
 'temperatura':24.5
 }
 ]

class SensorServer(SensorService_pb2_grpc.SensorServiceServicer):

  def RegistrarDadoSensor(self, request, context):
    dat = {
    'id':request.id,
    'data':request.data,
    'localizacao':request.localizacao,
    'temperatura':request.temperatura
    }
    tempDB.append(dat)
    return SensorService_pb2.StatusReply(status='OK')

  def ConsultarDadosSensoresPorData(self, request, context):
   list = SensorService_pb2.ListaDadosSensores()
    for item in tempDB 
        if (item['data'] == request.data):
            temp_data = SensorService_pb2.SensorData(id=item['id'], data=item['data'], localizacao=item['localizacao'], temperatura=item['temperatura']) 
            list.Sensor_data.append(temp_data)
    return list

  def ConsultarDadosSensoresPorLocalizacao(self, request, context):
   list = SensorService_pb2.ListaDadosSensores()
    for item in tempDB 
        if (item['localizacao'] == request.localizacao):
            temp_data = SensorService_pb2.SensorData(id=item['id'], data=item['data'], localizacao=item['localizacao'], temperatura=item['temperatura']) 
            list.Sensor_data.append(temp_data)
    return list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    SensorService_pb2_grpc.add_SensorServiceServicer_to_server(SensorServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()