#07_02_scipy_stats exercise
m_norm_0 = stats.multivariate_normal(m[['Apple', 'Microsoft', 'Intel']],
                                     df_incs[['Apple', 'Microsoft', 'Intel']].cov())
N_SIMS = 1000
daily_incs_0 = m_norm_0.rvs(size=[240, N_SIMS])
year_incs_0 = (daily_incs_0 + 1.).prod(axis=0)
earnings_0 = np.apply_along_axis(amount_to_pay, 1, year_incs_0)
print('Expected profit of the investment: {:.2%}'.format(earnings_0.mean()))
print('%5 higher risk of the investment: {:.2%}'.format(stats.scoreatpercentile(earnings_0, 95)))
print('%1 higher risk of the investment: {:.2%}'.format(stats.scoreatpercentile(earnings_0, 99)))