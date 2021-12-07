import time
import json

import redis
import requests

import urllib3.exceptions


class CompleteOrders:
    def __init__(self):
        self.subscriber = redis.Redis(host='redis', port=6379)
        self.channel = 'orders'
        self.pub_sub = self.subscriber.pubsub()
        self.pub_sub.subscribe(self.channel)
        self.api_url = "http://api:8000/api/v1/orders/confirm/"
        self.start_subscriber()

    def start_subscriber(self):
        while True:
            message = self.pub_sub.get_message()

            if message and not message['data'] == 1:
                data = json.loads(message['data'].decode('utf-8'))

                try:
                    requests.post(self.api_url, data=data, verify=False)
                except (urllib3.exceptions.NewConnectionError, requests.exceptions.ConnectionError):
                    requests.post(self.api_url, data=data, verify=False)


if __name__ == "__main__":
    CompleteOrders().start_subscriber()
