
from backtest_engine import BacktestEngine


def test_backtest():

    b=BacktestEngine()

    assert b.run()["status"]=="complete"
