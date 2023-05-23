from functools import lru_cache
from typing import Dict
from students.schema import Mark

marks_storage: Dict[int, list[Mark]] = {}

students = {}

@lru_cache()
def get_students():
    return students

@lru_cache()
def get_marks():
    return marks_storage