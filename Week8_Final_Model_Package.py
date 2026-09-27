#!/usr/bin/env python3
"""Week 8 Data Science: Final model package and baseline vs final comparison."""
import os
import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

WEEK8 = os.path.dirname(os.path.abspath(__file__))
WEEK6 = os.path.normpath(os.path.join(WEEK8, '..', 'week 6'))
WEEK7 = os.path.normpath(os.path.join(WEEK8, '..', 'week 7'))


def main():
    os.makedirs(WEEK8, exist_ok=True)

    # Load the metrics already computed in Weeks 6 and 7
    w6 = pd.read_csv(os.path.join(WEEK6, 'week6_model_metrics.csv'))
    w7 = pd.read_csv(os.path.join(WEEK7, 'week7_model_metrics.csv'))

    with open(os.path.join(WEEK7, 'week7_summary.json')) as f:
        summary = json.load(f)

    # Baseline vs final comparison at the default threshold
    rows = []
    for _, r in w7.iterrows():
        if 'Week 5 Baseline' in r['Model']:
            rows.append({'Stage': 'Week 5 Baseline', 'Model': 'Logistic Regression',
                         **r.to_dict()})
    for _, r in w6.iterrows():
        if 'Logistic Regression (Week 6)' in r['Model']:
            rows.append({'Stage': 'Week 6 Candidate', 'Model': 'Logistic Regression',
                         **r.to_dict()})
    for _, r in w7.iterrows():
        if 'Week 7 Best' in r['Model']:
            rows.append({'Stage': 'Week 7 Final', 'Model': 'Logistic Regression',
                         **r.to_dict()})

    comparison = pd.DataFrame(rows)
    comparison = comparison[['Stage', 'Model', 'Accuracy', 'Precision', 'Recall',
                             'F1', 'ROC_AUC', 'Brier']]
    comparison.to_csv(os.path.join(WEEK8, 'week8_baseline_vs_final_metrics.csv'),
                      index=False)
    print('Baseline vs final metrics:')
    print(comparison.to_string(index=False))

    # Cost-optimised threshold (0.28) performance from the final model
    cost_opt = summary['week6_candidate_at_028'].copy()
    cost_opt['Stage'] = 'Week 7 Final @ 0.28'
    cost_opt['Model'] = 'Logistic Regression'
    cost_opt_df = pd.DataFrame([cost_opt])
    cost_opt_df = cost_opt_df[['Stage', 'Model', 'Accuracy', 'Precision', 'Recall',
                                'F1', 'ROC_AUC', 'Brier']]
    cost_opt_df.to_csv(os.path.join(WEEK8, 'week8_threshold_0.28_metrics.csv'),
                       index=False)

    # Comparison plot
    x = np.arange(len(comparison))
    width = 0.35
    fig, ax = plt.subplots(figsize=(8, 5))
    bars1 = ax.bar(x - width/2, comparison['ROC_AUC'], width, label='ROC-AUC')
    bars2 = ax.bar(x + width/2, comparison['F1'], width, label='F1 (default threshold)')
    ax.set_ylabel('Score')
    ax.set_xticks(x)
    ax.set_xticklabels(comparison['Stage'], rotation=15, ha='right')
    ax.set_ylim(0, 1)
    ax.legend()
    ax.set_title('HealthConnect: Baseline vs Final Model Performance')
    for bar in bars1:
        ax.annotate(f'{bar.get_height():.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)
    for bar in bars2:
        ax.annotate(f'{bar.get_height():.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(WEEK8, 'week8_baseline_vs_final_performance.png'))
    plt.close()

    # Copy the final candidate predictions for the portfolio
    cand = pd.read_csv(os.path.join(WEEK7, 'week7_candidate_predictions.csv'))
    cand.to_csv(os.path.join(WEEK8, 'week8_final_predictions.csv'), index=False)

    # Final model selection statement
    with open(os.path.join(WEEK8, 'week8_final_model_selected.txt'), 'w') as f:
        f.write('Final selected model: Logistic Regression (improved_model_week7.pkl)\n')
        f.write(f"ROC-AUC: {summary['week6_candidate_metrics']['ROC_AUC']}\n")
        f.write(f"F1 at 0.28 threshold: {summary['week6_candidate_at_028']['F1']}\n")
        f.write(f"Optimal cost threshold: {summary['cost_optimal_threshold']}\n")

    # Machine-readable package summary
    pkg_summary = {
        'final_model': 'Logistic Regression (improved_model_week7.pkl)',
        'selected_features_n': 30,
        'roc_auc_test': summary['week6_candidate_metrics']['ROC_AUC'],
        'f1_at_0.28_test': summary['week6_candidate_at_028']['F1'],
        'cost_optimal_threshold': summary['cost_optimal_threshold'],
        'pipeline_test_passed': summary['pipeline_test_passed'],
        'n_test_records': summary['n_test_records']
    }
    with open(os.path.join(WEEK8, 'week8_final_model_summary.json'), 'w') as f:
        json.dump(pkg_summary, f, indent=2)
    print('Week 8 final model package files saved.')


if __name__ == '__main__':
    main()
