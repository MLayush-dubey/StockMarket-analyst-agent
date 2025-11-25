from crewai import Crew, Process
from agents.trader_agent import trader_agent
from agents.analyst_agent import analyst_agent
from tasks.trader_task import trading_task
from tasks.analyse_task import analyse_task


stock_market_crew = Crew(
    agents = [analyst_agent, trader_agent],
    tasks = [analyse_task, trading_task],
    process = Process.sequential,   #Analyst--> Trader
    verbose = True
)