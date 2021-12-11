import json
import redis


class RedisClient:
    def __init__(self):
        self.host = "redis"
        self.port = 6379
        self.db = 1
        self.redis_client = redis.StrictRedis(
            host=self.host,
            port=self.port,
            db=self.db
        )

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
