def ranked_voting(votes):
    candidate_points = {}  # Dictionary to store each candidate's points

    for vote in votes:
        for i, candidate in enumerate(vote):
            # Calculate points based on the ranking
            points = 3 - i  # 3 points for 1st place, 2 for 2nd, 1 for 3rd
            if candidate in candidate_points:
                candidate_points[candidate] += points
            else:
                candidate_points[candidate] = points

    # Sort candidates based on points in descending order and tie-breaker by appearance
    sorted_candidates = sorted(candidate_points.items(), key=lambda x: (x[1], votes.index(next(vote for vote in votes if x[0] in vote))))

    return [candidate for candidate, _ in sorted_candidates]

# Example usage:
votes = [
    ["alice", "bob", "charlie"],
    ["bob", "charlie", "alice"],
    ["charlie", "alice", "bob"],
    ["bob", "alice", "charlie"],
    ["charlie", "bob", "alice"],
    ["alice", "charlie", "bob"],
    ["dan", "bob", "alice"]
]

result = ranked_voting(votes)
print(result)
