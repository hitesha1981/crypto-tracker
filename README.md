# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-13 01:17 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | apr | 114.40% | $126,198,747 | $0.4974 |
| 2 | m | 66.70% | $383,597 | $1.2900 |
| 3 | cys | 47.20% | $73,021,306 | $1.6400 |
| 4 | btw | 24.50% | $50,568,402 | $0.2535 |
| 5 | velvet | 17.10% | $24,295,041 | $0.6514 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kaito | -28.90% | $88,344,504 | $0.4452 |
| 2 | holo | -15.10% | $55,751,278 | $0.0701 |
| 3 | beat | -12.80% | $89,653,042 | $0.9200 |
| 4 | arb | -7.60% | $43,305,537 | $0.0738 |
| 5 | 2z | -7.00% | $15,813,904 | $0.0486 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $32,834,920,555 | $0.9992 |
| 2 | btc | 0.00% | $22,233,016,175 | $63,559.0000 |
| 3 | usdc | 0.00% | $9,556,552,316 | $0.9995 |
| 4 | eth | 0.00% | $6,803,193,531 | $1,880.3800 |
| 5 | sol | -0.80% | $1,227,587,929 | $75.6700 |


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
