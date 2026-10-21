# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-21 02:46 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cvx | 22.02% | $22,297,323 | $2.5200 |
| 2 | comp | 20.67% | $124,461,138 | $25.6600 |
| 3 | hash | 15.47% | $41,952 | $0.0075 |
| 4 | cards | 14.28% | $28,754,992 | $0.3617 |
| 5 | useless | 11.73% | $17,217,741 | $0.1583 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | grx | -21.35% | $2,668,261 | $15.9400 |
| 2 | mx | -10.56% | $8,853,517 | $1.7200 |
| 3 | morpho | -6.02% | $25,518,874 | $2.3100 |
| 4 | q | -5.24% | $15,062,990 | $0.1180 |
| 5 | xmr | -3.90% | $181,462,836 | $576.2300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $51,170,859,433 | $0.9992 |
| 2 | btc | 1.38% | $27,653,377,689 | $82,712.0000 |
| 3 | usdc | -0.02% | $15,073,793,747 | $0.9997 |
| 4 | eth | 2.24% | $11,670,803,725 | $2,446.6900 |
| 5 | sol | 1.32% | $2,717,917,195 | $106.1300 |


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
