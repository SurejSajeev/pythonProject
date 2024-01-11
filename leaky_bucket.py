class LeakyBucket:
    def __init__(self, bucket_size, output_size):
        self.bucket_size = bucket_size
        self.output_size = output_size

    def start_leak(self, traffic_list):
        storage = 0
        for traffic in traffic_list:
            size_left = self.bucket_size - storage
            if traffic <= size_left:
                storage += traffic
                print(f"Processing {traffic} with remaining storage at {storage}")
            else:
                print(f"Packet loss for {traffic} with storage {storage}")
            storage -= self.output_size


if __name__ == '__main__':
    lb = LeakyBucket(10, 1)
    lb.start_leak([2,3,4,5])

