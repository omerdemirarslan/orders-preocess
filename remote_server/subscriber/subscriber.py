import time
import json

import redis
import requests

import urllib3.exceptions


class SendOrders:
    def __init__(self):
        self.subscriber = redis.Redis(host='redis', port=6379)
        self.channel = 'orders'
        self.pub_sub = subscriber.pubsub()
        self.pub_sub.subscribe(channel)
        self.api_url = "http://app:8000/api/v1/order/get-order/"

        while True:
            message = self.pub_sub.get_message()

            if message and not message['data'] == 1:
                data = json.loads(message['data'].decode('utf-8'))

                try:
                    time.sleep(10)
                    requests.post(self.api_url, data=data)
                except (urllib3.exceptions.NewConnectionError, requests.exceptions.ConnectionError):
                    time.sleep(10)
                    requests.put(self.api_url, data=data)
