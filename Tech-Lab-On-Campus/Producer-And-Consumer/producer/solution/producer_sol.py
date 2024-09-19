from producer_interface import mqProducerInterface
import pika
import os

class mqProducer(mqProducerInterface):
    def __init__ (self, routing_key: str, exchange_name: str):
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.m_connection = pika.BlockingConnection(parameters=con_params)

        self.m_channel = self.m_connection.channel()

        self.m_channel.exchange_declare(self.exchange_name)

        

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.m_channel.basic_publish(self.exchange_name, self.routing_key, 'Hi...')
        
        # Close Channel
        self.m_channel.close()

        # Close Connection
        self.m_connection.close()
        pass
