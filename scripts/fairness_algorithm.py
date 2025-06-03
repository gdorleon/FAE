import numpy as np

def enforce_fairness(rel_matrix, item_groups, delta=0.1, top_k=5):
    num_users, num_items = rel_matrix.shape
    group_ids = list(set(item_groups.values()))
    user_recommendations = {}
    exposure = {u: {g: 0 for g in group_ids} for u in range(num_users)}

    for u in range(num_users):
        top_items = rel_matrix[u].argsort()[::-1]
        selected = []
        group_exposure = {g: 0 for g in group_ids}

        for i in top_items:
            group = item_groups[i]
            if len(selected) < top_k and (group_exposure[group] / (len(selected) + 1) <= delta or len(selected) == 0):
                selected.append(i)
                group_exposure[group] += 1
            if len(selected) == top_k:
                break

        user_recommendations[u] = selected
        for i in selected:
            g = item_groups[i]
            exposure[u][g] += 1

    return user_recommendations, exposure
