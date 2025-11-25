from crew import stock_market_crew

def run(stock: str):
    result = stock_market_crew.kickoff(inputs={"stock": stock})
    print(result)

if __name__ == "__main__":
    run(stock="Apple")