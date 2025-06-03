import numpy as np
import pandas as pd

def generate_synthetic_data(num_users=100, num_items=50, num_groups=5, boost=0.5, seed=42):
    np.random.seed(seed)
    items_per_group = num_items // num_groups
    item_ids = np.arange(num_items)
    item_groups = {i: i // items_per_group for i in item_ids}

    user_group_preference = np.random.choice(num_groups, size=num_users)
    relevance_matrix = np.random.rand(num_users, num_items)

    for u in range(num_users):
        preferred_group = user_group_preference[u]
        for i in range(num_items):
            if item_groups[i] == preferred_group:
                relevance_matrix[u, i] += boost

    relevance_matrix = np.clip(relevance_matrix, 0, 1)
    rel_df = pd.DataFrame(relevance_matrix, columns=[f"Item_{i}" for i in range(num_items)])
    rel_df.insert(0, 'User', [f"User_{u}" for u in range(num_users)])

    item_group_df = pd.DataFrame({
        'Item': [f"Item_{i}" for i in range(num_items)],
        'Group': [item_groups[i] for i in range(num_items)]
    })

    return rel_df, item_group_df, item_groups

if __name__ == "__main__":
    rel_df, item_group_df, item_groups = generate_synthetic_data()
    rel_df.to_csv("data/synthetic_dataset.csv", index=False)
    item_group_df.to_csv("data/item_groups.csv", index=False)
    print("Synthetic data generated and saved.")
