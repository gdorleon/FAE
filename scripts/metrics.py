import numpy as np

def compute_utility(rel_matrix, recommendations):
    total = 0.0
    for u, items in recommendations.items():
        total += sum(rel_matrix[u][i] for i in items)
    return total

def compute_exposure_disparity(exposure):
    group_ids = list(next(iter(exposure.values())).keys())
    max_disparity = 0
    for g in group_ids:
        vals = [exposure[u][g] for u in exposure]
        disparity = max(vals) - min(vals)
        max_disparity = max(max_disparity, disparity)
    return max_disparity

def compute_envy(rel_matrix, recommendations):
    envy_count = 0
    for u in recommendations:
        own_utility = sum(rel_matrix[u][i] for i in recommendations[u])
        for v in recommendations:
            if u == v:
                continue
            other_utility = sum(rel_matrix[u][i] for i in recommendations[v])
            if other_utility > own_utility:
                envy_count += 1
                break
    return envy_count
