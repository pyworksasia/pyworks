# from App.Services.RedisManager.redisdb import RedisManager
import redis
import sys
import json
from datetime import timedelta


class RedisRepository():

	def __init__(self):
		self.client = self.connection()

	def connection(self) -> redis.client.Redis:
		try:
			client = redis.Redis(
				host="localhost",
				port=6379,
				password="ubuntu",
				db=0,
				socket_timeout=5,
			)
			ping = client.ping()
			if ping is True:
				return client
		except redis.AuthenticationError:
			print("AuthenticationError")
			sys.exit(1)

	def create(self, key: str, value: dict) -> bool:
		"""Set data to redis."""
		value = json.dumps(value)
		state = self.client.setex(key, timedelta(seconds=3600), value=value, )
		return state

	def find(self, key):
		"""Get data from redis."""
		value = self.client.get(key)
		return json.loads(value)


