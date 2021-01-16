# -*- coding: utf-8 -*-

import pickle

from redis import Redis

from .cache_abstract import CacheAbstract


class RedisCache(CacheAbstract):
    """Redis 缓存"""

    # 默认的缓存地址
    default_redis_url = "redis://localhost:6379/0"

    def __init__(self, redis_url=None):
        redis_url = redis_url or self.default_redis_url
        self.redis = Redis.from_url(redis_url)

    def set(self, key, value, expire=-1):
        if expire == -1:
            expire = None

        value = pickle.dumps(value)
        self.redis.set(key, value, expire)

    def get(self, key):
        value = self.redis.get(key)

        if value:
            return pickle.loads(value)
