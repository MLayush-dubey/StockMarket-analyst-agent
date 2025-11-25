import yfinance as yf
from crewai.tools import tool

@tool("Live Stock Information Tool")
def stock_market_tool(stock_symbol: str)-> str:
    """
    Retrieves the stock price and other relevant info for a given stock symbol using Yahoo Finance.

    Parameters:
    stock_symbol(str): The ticker symbol of the stock(eg- AAPL, TSLA, MSFT)

    Return:
        str: Summary of the stock's current price, daily change and prediction for next week
    """

    stock = yf.Ticker(stock_symbol)
    info = stock.info

    # Current Price Data
    current_price = info.get('regularMarketPrice', info.get('currentPrice'))
    change = info.get('regularMarketChange')
    change_percent = info.get('regularMarketChangePercent')
    currency = info.get('currency', 'USD')

    # Valuation Metrics
    trailing_pe = info.get('trailingPE')
    forward_pe = info.get('forwardPE')
    peg_ratio = info.get('pegRatio')

    # Growth Indicators
    revenue_growth = info.get('revenueGrowth')
    earnings_growth = info.get('earningsGrowth')

    # Profitability
    profit_margin = info.get('profitMargins')
    roe = info.get('returnOnEquity')

    # Analyst Predictions (KEY for forecasting!)
    target_mean = info.get('targetMeanPrice')
    target_high = info.get('targetHighPrice')
    target_low = info.get('targetLowPrice')
    recommendation = info.get('recommendationKey')
    num_analysts = info.get('numberOfAnalystOpinions')

    # Risk Metrics
    beta = info.get('beta')
    week_52_high = info.get('fiftyTwoWeekHigh')
    week_52_low = info.get('fiftyTwoWeekLow')

    # Financial Health
    debt_to_equity = info.get('debtToEquity')
    current_ratio = info.get('currentRatio')
    free_cashflow = info.get('freeCashflow')

    # Build comprehensive summary
    summary = f"""
    Stock: {stock_symbol}
    Current Price: {current_price} {currency} (Change: {change_percent:.2f}%)

    VALUATION:
    - P/E Ratio (Trailing): {trailing_pe}
    - P/E Ratio (Forward): {forward_pe}
    - PEG Ratio: {peg_ratio}

    GROWTH:
    - Revenue Growth: {revenue_growth:.2%} if revenue_growth else 'N/A'
    - Earnings Growth: {earnings_growth:.2%} if earnings_growth else 'N/A'

    PROFITABILITY:
    - Profit Margin: {profit_margin:.2%} if profit_margin else 'N/A'
    - Return on Equity: {roe:.2%} if roe else 'N/A'

    ANALYST PREDICTIONS (Next 12 months):
    - Target Mean Price: {target_mean} {currency}
    - Target Range: {target_low} - {target_high} {currency}
    - Recommendation: {recommendation.upper() if recommendation else 'N/A'}
    - Number of Analysts: {num_analysts}

    RISK PROFILE:
    - Beta: {beta} (Volatility vs market)
    - 52-Week Range: {week_52_low} - {week_52_high}

    FINANCIAL HEALTH:
    - Debt/Equity: {debt_to_equity}
    - Current Ratio: {current_ratio}
    - Free Cash Flow: {free_cashflow:,} if free_cashflow else 'N/A'
    """

    return summary

print(stock_market_tool('AAPL'))