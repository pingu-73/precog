import numpy as np
from numpy import dot
from numpy.linalg import norm
from annoy import AnnoyIndex

def cosine(v1, v2):
    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0
    

def fast_cosine(v1, v2):
    if norm(v1) > 0 and norm(v2) > 0:
        f = len(v1)
        t = AnnoyIndex(f, 'angular')  
        t.add_item(0, v1)
        t.add_item(1, v2)
        t.build(10)
        return (1 - t.get_distance(0, 1)) # 1 - cosine distance = cosine similarity
    else:
        return 0.0