class HashTable:
  def __init__(self, bucket_size = 256):
    self.bucket_size = bucket_size
    self.hash_table = self.create_buckets()

  def create_buckets(self):
    return [[] for _ in range(self.bucket_size)]

  def set_value(self, key, value):
    hashed_key = hash(value) % self.bucket_size
    print(f'Hashed-key: {hashed_key}, Value at this key: {self.hash_table[hashed_key]}')

  def get_value(self, key):
    pass

  def __str__(self):
    pass