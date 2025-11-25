from crewai import Task
from agents.analyst_agent import analyst_agent

analyse_task = Task(
    agent = analyst_agent,
    description = (
        "Analyze {stock_symbol} using comprehensive financial metrics. "
        "Evaluate P/E ratio, revenue growth, profitability margins, debt levels, "
        "analyst predictions, and compare to industry peers. Determine if the stock "
        "is overvalued, fairly valued, or undervalued. Provide investment thesis."
    ),
    expected_output= (
        "Detailed financial analysis report with valuation assessment, "
        "key strengths/weaknesses, and overall investment recommendation "
        "(Strong Buy/Buy/Hold/Sell)."
    ),
)