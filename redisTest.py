
import redis

redis_cli = redis.StrictRedis()

redis_cli.set('cs',100)

print(redis_cli.get('cs'))

redis_cli.close()

nums = [1,2,3]
for i in range(3):
    if i == 1:
        print(nums[i])