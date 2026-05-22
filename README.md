# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-22 02:41 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | grass | 27.54% | $37,595,422 | $0.4249 |
| 2 | near | 21.37% | $667,341,938 | $2.0900 |
| 3 | beat | 17.20% | $30,239,048 | $0.7553 |
| 4 | vvv | 14.28% | $103,147,186 | $19.0700 |
| 5 | aero | 11.45% | $43,721,517 | $0.4648 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usda | -20.62% | $705 | $0.7803 |
| 2 | ub | -17.64% | $18,501,077 | $0.0945 |
| 3 | b | -16.11% | $36,751,544 | $0.2954 |
| 4 | gwei | -10.14% | $5,945,690 | $0.1161 |
| 5 | bsb | -9.81% | $80,683,500 | $0.9460 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $51,099,992,581 | $0.9990 |
| 2 | btc | -0.47% | $26,860,873,978 | $77,564.0000 |
| 3 | eth | -0.43% | $12,766,636,700 | $2,133.1600 |
| 4 | usdc | 0.01% | $12,318,479,958 | $0.9997 |
| 5 | sol | 0.32% | $2,957,358,847 | $86.9700 |


<!-- END_DYNAMIC_CONTENT -->

## How to generate the coingecko demo public api key

[coingecko-api-key-docs](https://support.coingecko.com/hc/en-us/articles/21880397454233-User-Guide-How-to-sign-up-for-CoinGecko-Demo-API-and-generate-an-API-key)

## Requirements to setup
## 1. Install uv

```bash
brew install uv
✔︎ JSON API cask.jws.json                                                                                                                                                       [Downloaded   15.1MB/ 15.1MB]
✔︎ JSON API formula.jws.json                                                                                                                                                    [Downloaded   32.1MB/ 32.1MB]
# or Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 2. Setup Python Environment (uv)

From the project root:

```bash
uv python install 3.12
uv venv --python 3.12
source .venv/bin/activate
```

Install dependencies (locked):
```bash
uv add pandas requests matplotlib python-dotenv
```


---

## 4. Update coingecko demo key in .env ( I have provided in .env.sample)
```bash
cat .env
CGK_API_DEMO_KEY="Your-coingecko-demo-api-key-here"
```

---

## 3. To manually run the script
```bash
python3.12 main.py
```
---
