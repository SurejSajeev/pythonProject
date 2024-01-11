def rankTeams(votes):
    vote_count = {team: [0] * len(votes[0]) for team in votes[0]}

    for vote in votes:
        for i, team in enumerate(vote):
            vote_count[team][i] -= 1

    sorted_teams = sorted(votes[0], key=lambda team: (vote_count[team], team))

    return ''.join(sorted_teams)


# Example usage:
votes1 = ["ABC", "ACB", "ABC", "ACB", "ACB"]
votes2 = ["WXYZ", "XYZW"]
votes3 = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]

print(rankTeams(votes1))  # Output: "ACB"
print(rankTeams(votes2))  # Output: "XWYZ"
print(rankTeams(votes3))  # Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
