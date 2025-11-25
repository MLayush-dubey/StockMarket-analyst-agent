from crewai import Task
from agents.trader_agent import trader_agent


trading_task = Task(
    agent = trader_agent,
    description = (
        "Based on the analyst's research on {stock}, develop a concrete "
        "trading strategy. Specify: \n"
        "1. Action: BUY/SELL/HOLD\n"
        "2. Entry price target and optimal timing\n"
        "3. Position size (% of portfolio)\n"
        "4. Stop-loss level (downside protection)\n"
        "5. Take-profit targets (profit booking levels)\n"
        "6. Risk-reward ratio\n"
        "7. Time horizon (day/swing/position trade)"
    ),
    expected_output= (
        "Executable trading plan with specific entry/exit points, position sizing, "
        "and risk management parameters. Include alternative scenarios for different "
        "market conditions."
    ),
)