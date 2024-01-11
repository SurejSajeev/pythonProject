import time


class RateLimiter:

    def __init__(self, no_of_req, req_per_second):
        self.no_of_req = no_of_req
        self.req_per_second = req_per_second
        self.req_list = []

    def make_new_req(self):
        curr_time = int(time.time())

        while self.req_list and self.req_list[0] <= (curr_time - self.no_of_req):
            self.req_list.pop(0)

        if len(self.req_list) <= self.no_of_req:
            self.req_list.append(curr_time)
            return True
        else:
            return False


if __name__ == '__main__':
    rate_limiter = RateLimiter(no_of_req=5, req_per_second=60)

    customer_id = 123

    for _ in range(10):
        if rate_limiter.make_new_req():
            print("Request allowed")
        else:
            print("Request rate limited")