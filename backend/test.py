from scipy import stats

# Degrees of freedom (df = n - 1)
n = 10  # Sample size
df = n - 1

# Significance level (for one-tailed test)
alpha = 0.05

# Critical value (one-tailed t-distribution)
critical_value = stats.t.ppf(1 - alpha, df)
print(f"Critical value for one-tailed t-test: {critical_value}")
critical_value_two_tailed = stats.t.ppf(1 - alpha / 2, df)
print(f"Critical value for two-tailed t-test: ±{critical_value_two_tailed}")
