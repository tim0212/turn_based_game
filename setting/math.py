import math, os, pygame

inf = math.inf

def limit(val, min_val: int, max_val: int):
  return max(min_val, min(val, max_val))