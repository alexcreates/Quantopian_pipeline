import pyfolio as pf
import matplotlib.pyplot as plt
import empyrical

"""
This is designed for using Quantopian's
Backtest and Benchmark Platform. This is
done by grabbing the hash from the url once
the Backtest and Benchmarks have been run.
PyFolio.py has the ability to print out the
results, plots and graphs. There are 9 forms
of results including a Round Trip Tear-sheet



Insert Hash's at both get_backtest method calls
"""


# Process the Trading Algo results
backtest = get_backtest('insert backtest hash')
backtest_returns = backtest.daily_performance['returns']
backtest_positions = backtest.pyfolio_positions
backtest_transactions = backtest.pyfolio_transactions

# Process the Benchmark Results to Normalize the data and have a comparison
benchmark = get_backtest('insert benchmark hash')
benchmark_returns = benchmark.daily_performance['returns']
benchmark_positions = benchmark.pyfolio_positions
benchmark_transactions = benchmark.pyfolio_transactions



##################################
#          Sharpe Ratio          #
#   for backtest and benchmark   #
#         Combined Beta          #
##################################
backtest_sharpe = empyrical.sharpe_ratio(backtest_returns)
benchmark_sharpe = empyrical.sharpe_ratio(benchmark_returns)

combined_beta = empyrical.beta(backtest_returns, benchmark_returns)


############################
#         Round Trip       #
#         Tear Sheet       #
#      right = positive    #
#      left = negative     #
############################
tear_sheet = pf.create_round_trip_tear_sheet(backtest_returns, backtest_positions, backtest_transactions)

# Cumulative Returns
plt.subplot(2,1,1)
pf.plotting.plot_rolling_returns(backtest_returns, benchmark_returns)

# Daily, Non-Cumulative Returns
plt.subplot(2,1,2)
pf.plotting.plot_returns(backtest_returns)
plt.tight_layout()


fig = plt.figure(1)
############################
#      Horizontal Graph    #
#     frequency = Annual   #
#      right = positive    #
#      left = negative     #
############################
plt.subplot(1,3,1)
pf.plot_annual_returns(backtest_returns)


############################
#       Veritcal Graph     #
#        Distribution      #
#    frequency = Monthly   #
#      right = positive    #
#      left = negative     #
############################
plt.subplot(1,3,2)
pf.plot_monthly_returns_dist(backtest_returns)


############################
#       Veritcal Graph     #
#          HeatMap         #
#    frequency = Month/Yr  #
#      green = positive    #
#       red = negative     #
############################
plt.subplot(1,3,3)
pf.plot_monthly_returns_heatmap(backtest_returns)

plt.tight_layout()
fig.set_size_inches(15,5)


############################
#        Candle Plot       #
#     frequency = D/W/M    #
#          Returns         #
############################
pf.plot_return_quantiles(backtest_returns)


############################
#        Rolling Plot      #
#      frequency = M/Y     #
#            BETA          #
############################
pf.plot_rolling_beta(backtest_returns, benchmark_returns)


############################
#        Rolling Plot      #
#      frequency = M/Y     #
#        SHARPE RATIO      #
############################
pf.plot_rolling_sharpe(backtest_returns)


############################
#  Top 10 Drawdown Periods #
#      frequency = M/Y     #
############################
pf.plot_drawdown_periods(backtest_returns)


############################
#      UnderWater Plot     #
#      Drawdown Periods    #
#      frequency = M/Y     #
#      in values of = %    #
############################
pf.plot_drawdown_underwater(backtest_returns)
