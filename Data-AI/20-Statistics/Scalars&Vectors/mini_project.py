import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# User preferences
user = np.array([5, 1, 0])

# Items
movie1 = np.array([4, 1, 0])
movie2 = np.array([1, 5, 5])
movie3 = np.array([5, 1, 1])

movies = [movie1, movie2, movie3]

# Compute similarity
scores = []
for i, movie in enumerate(movies):
    sim = cosine_similarity(user, movie)
    scores.append((i, sim))

# Sort
scores.sort(key=lambda x: x[1], reverse=True)

print("Recommendations (best to worst):")
for index, score in scores:
    print(f"Movie {index+1}: Score = {score:.4f}")