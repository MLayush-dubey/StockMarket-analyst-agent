# 📈 Stock Market Analyst Agent

An intelligent multi-agent system powered by CrewAI and Google Gemini that provides comprehensive stock analysis and actionable trading strategies. The system combines deep financial analysis with professional trading expertise to deliver data-driven investment recommendations.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-orange.svg)](https://www.crewai.com/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Pro-4285F4.svg)](https://deepmind.google/technologies/gemini/)
[![Yahoo Finance](https://img.shields.io/badge/Data-Yahoo%20Finance-purple.svg)](https://finance.yahoo.com/)

## 🌟 Key Features

- **Dual-Agent Architecture**: Specialized analyst and trader agents working in sequential collaboration
- **Real-Time Market Data**: Live stock information via Yahoo Finance API integration
- **Comprehensive Analysis**: Evaluates 15+ financial metrics including P/E ratios, growth indicators, and analyst predictions
- **Actionable Trading Plans**: Generates specific entry/exit points, position sizing, and risk management parameters
- **Deterministic Results**: Configured for reproducible analysis with temperature=0 and fixed seed
- **Production-Ready**: Built with enterprise-grade LLM configuration including retries and timeout handling

## 🏗️ System Architecture

```
Stock Market Analyst Agent/
├── agents/
│   ├── analyst_agent.py      # Financial analysis specialist
│   └── trader_agent.py        # Trading strategy expert
├── tasks/
│   ├── analyse_task.py        # Deep-dive stock analysis
│   └── trader_task.py         # Executable trading strategy
├── tools/
│   └── stock_research_tool.py # Yahoo Finance integration
├── crew.py                     # Agent orchestration
├── main.py                     # Entry point
├── requirements.txt            # Dependencies
└── .env                        # API configuration
```

### Agent Workflow

```
User Input (Stock Symbol)
         ↓
   Analyst Agent
   - Retrieves live market data
   - Analyzes financial metrics
   - Evaluates valuation
   - Generates recommendation
         ↓
   Trader Agent
   - Develops trading strategy
   - Sets entry/exit points
   - Calculates position sizing
   - Defines risk management
         ↓
   Final Trading Plan
```

## 🤖 Meet the Agents

### 1. **Analyst Agent** - The Research Expert

**Profile**: Veteran quantitative analyst with 15+ years at top investment banks

**Capabilities**:
- Fundamental analysis using 15+ financial metrics
- Valuation assessment (P/E, PEG, debt ratios)
- Growth trend analysis (revenue, earnings)
- Profitability evaluation (margins, ROE)
- Risk profiling (beta, 52-week ranges)
- Analyst consensus synthesis
- Buy/Hold/Sell recommendations

**Tools**: Live Stock Information Tool (Yahoo Finance)

### 2. **Trader Agent** - The Execution Specialist

**Profile**: Seasoned institutional trader with 20+ years in hedge funds

**Capabilities**:
- Actionable trading strategy development
- Precise entry/exit point calculation
- Position sizing based on risk tolerance
- Stop-loss and take-profit level setting
- Risk-reward ratio optimization
- Multi-scenario planning
- Time horizon determination

**Tools**: Analyst insights (receives sequential output)

## 📊 Financial Metrics Analyzed

The system evaluates comprehensive market data:

| Category | Metrics |
|----------|---------|
| **Valuation** | Trailing P/E, Forward P/E, PEG Ratio |
| **Growth** | Revenue Growth, Earnings Growth |
| **Profitability** | Profit Margin, Return on Equity |
| **Predictions** | Analyst Target Prices, Recommendations |
| **Risk** | Beta, 52-Week High/Low, Volatility |
| **Health** | Debt-to-Equity, Current Ratio, Free Cash Flow |

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/MLayush-dubey/StockMarket-analyst-agent.git
cd StockMarket-analyst-agent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**

Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Usage

**Basic Usage**:
```bash
python main.py
```

**Analyze a Specific Stock**:

Edit `main.py` to change the stock symbol:
```python
if __name__ == "__main__":
    run(stock="TSLA")  # Analyze Tesla
    # run(stock="MSFT")  # Analyze Microsoft
    # run(stock="GOOGL") # Analyze Google
```

Or modify the `run()` function call directly:
```bash
python -c "from main import run; run('AAPL')"
```

### Example Output

```
Stock: AAPL
Current Price: 178.52 USD (Change: +1.23%)

VALUATION:
- P/E Ratio (Trailing): 29.4
- P/E Ratio (Forward): 27.8
- PEG Ratio: 2.1

ANALYST PREDICTIONS:
- Target Mean Price: 195.00 USD
- Recommendation: BUY
- Number of Analysts: 42

========================================
ANALYST RECOMMENDATION: Strong Buy
========================================

TRADING STRATEGY:
Action: BUY
Entry Price: $177.50 - $179.00
Position Size: 5% of portfolio
Stop-Loss: $170.00 (4.5% downside protection)
Take-Profit: $195.00 (Target), $210.00 (Stretch)
Risk-Reward Ratio: 1:3.2
Time Horizon: 3-6 months (Position trade)
```

## 🔧 Configuration

### LLM Parameters

Both agents use optimized Gemini 2.5 Pro configuration:

```python
llm = LLM(
    model="gemini/gemini-2.5-pro",
    temperature=0,        # Deterministic analysis
    api_key=os.getenv("GEMINI_API_KEY"),
    max_retries=3,        # Resilience to API issues
    top_p=0.9,            # Balanced vocabulary
    timeout=180.0,        # 3-minute timeout
    seed=42               # Reproducible results
)
```

### Customizing Agent Behavior

**Adjust Analysis Depth** (in `tasks/analyse_task.py`):
```python
description = (
    "Analyze {stock} focusing on [YOUR SPECIFIC CRITERIA]. "
    "Compare with competitors [COMPETITOR_LIST]."
)
```

**Modify Trading Strategy** (in `tasks/trader_task.py`):
```python
description = (
    "Develop a [DAY/SWING/LONG-TERM] trading strategy for {stock}. "
    "Target risk-reward ratio of [YOUR_RATIO]."
)
```

## 🛠️ Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | CrewAI | Multi-agent orchestration |
| **LLM** | Google Gemini 2.5 Pro | Natural language understanding |
| **Market Data** | Yahoo Finance (yfinance) | Real-time stock information |
| **Process** | Sequential | Analyst → Trader workflow |
| **Memory** | CrewAI Memory | Context retention across tasks |

## 📈 Use Cases

1. **Individual Investors**: Get professional-grade analysis before making investment decisions
2. **Portfolio Management**: Evaluate multiple stocks systematically
3. **Learning Tool**: Understand what metrics professional analysts consider
4. **Automated Screening**: Run batch analysis on watchlists
5. **Research Validation**: Cross-check your own analysis with AI-powered insights


### Tool Integration

Custom CrewAI tool decorator for Yahoo Finance:
```python
@tool("Live Stock Information Tool")
def stock_market_tool(stock: str) -> str:
    """Retrieves comprehensive stock data"""
    # 15+ financial metrics extraction
```

## ⚠️ Limitations & Disclaimers

- **Not Financial Advice**: This tool provides analysis for educational purposes only
- **Market Data Delay**: Yahoo Finance data may have minor delays
- **Historical Performance**: Past analysis does not guarantee future results
- **Risk Management**: Always conduct your own due diligence before investing
- **API Dependencies**: Requires active internet connection and valid API keys


## 🐛 Troubleshooting

### Common Issues

**Problem**: `GEMINI_API_KEY not found`
```bash
# Solution: Ensure .env file exists with valid key
echo "GEMINI_API_KEY=your_key_here" > .env
```

**Problem**: `Stock data not available`
```bash
# Solution: Verify ticker symbol is correct and the variable used are same everywhere.
# Use Yahoo Finance symbol (e.g., AAPL not Apple)
```

**Problem**: API timeout errors
```bash
# Solution: Increase timeout in agent configuration
timeout=300.0  # 5 minutes
```

**Problem**: Rate limiting from Yahoo Finance
```bash
# Solution: Add delays between requests
import time
time.sleep(1)  # Wait 1 second between stocks
```

## 🛣️ Roadmap

- [ ] Multi-stock comparison analysis
- [ ] Technical indicators integration (RSI, MACD, Moving Averages)
- [ ] Sentiment analysis from news and social media
- [ ] Web interface (Streamlit/Gradio)--> I will be building a frontend soon
- [ ] Real-time alerts for price targets

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

1. Additional financial metrics
2. More sophisticated trading strategies
3. Integration with other data sources
4. Performance optimization

**How to Contribute**:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Learning Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [Google Gemini API](https://ai.google.dev/docs)
- [Yahoo Finance API](https://pypi.org/project/yfinance/)
- [Technical Analysis Basics](https://www.investopedia.com/technical-analysis-4689657)


## 🙏 Acknowledgments

- **CrewAI** - Powerful multi-agent framework
- **Google Gemini** - State-of-the-art LLM capabilities
- **Yahoo Finance** - Reliable market data API
- Financial analysis community for best practices

## 📧 Contact

For questions, issues, or collaboration:
- Open an issue on GitHub
- Submit a pull request
- Star the repository if you find it useful!

---

⚠️ **DISCLAIMER**: This software is for educational and informational purposes only. It does not constitute financial advice, investment advice, trading advice, or any other sort of advice. You should not treat any of the tool's output as such. Always conduct your own research and consult with a licensed financial advisor before making any investment decisions.

**Built with 🤖 for Smart Investors**
