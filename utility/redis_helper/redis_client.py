import json
import redis


class RedisClient:
    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host='redis',
            port=6379,
            db=1
        )

    def get_client(self):
        """
        This Method Return Redis Client
        :return:
        """
        return self.redis_client

    def publish_data_on_redis(self, json_data: dict, channel_name: str) -> bool:
        """
        This Method Publishing Data To Redis Client
        :param json_data:
        :param channel_name:
        :return:
        """
        self.redis_client.publish(
            channel=channel_name,
            message=json.dumps(json_data)
        )

        return True
