from functools import lru_cache

students = {}

@lru_cache()
def get_students():
    return students