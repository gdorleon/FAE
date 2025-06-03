import pandas as pd
import numpy as np
from src.simulate_data import generate_synthetic_data
from src.fairness_algorithm import enforce_fairness
from src.metrics import compute_utility, compute_exposure_disparity, compute_envy

if __name__ == "__main__":
    # Generate synthetic data
    rel_df, item_group_df, item_groups = generate_synthetic_data()
    rel_matrix = rel_df.drop(columns=['User']).to_numpy()

    # Run Fairness Enforcement Algorithm
    recommendations, exposure = enforce_fairness(rel_matrix, item_groups, delta=0.1, top_k=5)

    # Compute metrics
    utility = compute_utility(rel_matrix, recommendations)
    disparity = compute_exposure_disparity(exposure)
    envy_count = compute_envy(rel_matrix, recommendations)

    # Print results
    print("--- Fairness Evaluation Results ---")
    print(f"Total Utility: {utility:.3f}")
    print(f"Max Exposure Disparity: {disparity}")
    print(f"Users with Envy: {envy_count}")

    # Save results
    pd.DataFrame.from_dict(exposure, orient='index').to_csv("results/exposure_matrix.csv")
    print("Exposure matrix saved to results/exposure_matrix.csv")
