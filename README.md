# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-28 01:16 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ftn | 110.48% | $13,620,506 | $1.0470 |
| 2 | zec | 15.81% | $889,212,036 | $517.5200 |
| 3 | cc | 15.28% | $20,285,796 | $0.1137 |
| 4 | dash | 12.95% | $181,423,959 | $44.3600 |
| 5 | stable | 10.39% | $42,315,563 | $0.0136 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | merl | -14.22% | $19,174,810 | $0.3668 |
| 2 | qrl | -12.95% | $515,235 | $3.0000 |
| 3 | mon | -3.33% | $98,655,931 | $0.0228 |
| 4 | tel | -3.16% | $2,670,651 | $0.0042 |
| 5 | pippin | -3.13% | $21,246,271 | $0.4719 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $30,494,932,887 | $0.9994 |
| 2 | btc | 0.53% | $15,718,499,670 | $87,791.0000 |
| 3 | eth | 0.77% | $8,746,652,034 | $2,944.0100 |
| 4 | usdc | 0.23% | $3,812,509,937 | $1.0020 |
| 5 | sol | 2.01% | $1,866,304,623 | $124.3600 |


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
