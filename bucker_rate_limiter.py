import time


class TokenBucketRateLimiter:
    def __init__(self, capacity, refill_rate, time_interval):
        self.capacity = capacity
        self.tokens = capacity  # Initially, the bucket is full
        self.refill_rate = refill_rate
        self.last_refill_time = time.time()
        self.time_interval = time_interval

    def _refill(self):
        now = time.time()
        elapsed_time = now - self.last_refill_time
        tokens_to_add = elapsed_time * self.refill_rate

        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_time = now

    def acquire(self, tokens=1):
        self._refill()

        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        else:
            return False


# Example usage:
rate_limiter = TokenBucketRateLimiter(capacity=10, refill_rate=2, time_interval=1)

for i in range(15):
    if rate_limiter.acquire():
        print(f"Request {i + 1}: Allowed")
    else:
        print(f"Request {i + 1}: Rate Limited")
