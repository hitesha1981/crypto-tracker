# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-19 02:37 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | 9bit | 31.31% | $11,016,559 | $0.0341 |
| 2 | bsb | 26.77% | $31,668,195 | $0.6777 |
| 3 | mbtc | 17.65% | $39,351 | $0.1887 |
| 4 | trac | 16.95% | $116,416,095 | $0.3785 |
| 5 | ondo | 15.20% | $220,179,481 | $0.3925 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xp | -22.19% | $3,161,308 | $0.0481 |
| 2 | bill | -12.88% | $150,681,974 | $0.1353 |
| 3 | ub | -12.62% | $19,389,455 | $0.1349 |
| 4 | asteroid | -7.71% | $14,749,844 | $0.0003 |
| 5 | flr | -7.52% | $3,803,184 | $0.0083 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $67,563,132,236 | $0.9992 |
| 2 | btc | -0.13% | $42,407,045,791 | $76,735.0000 |
| 3 | eth | 0.57% | $17,108,297,380 | $2,126.7600 |
| 4 | usdc | -0.01% | $15,554,370,798 | $0.9997 |
| 5 | sol | 0.07% | $2,896,350,602 | $84.9600 |


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
