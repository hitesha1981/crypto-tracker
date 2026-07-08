# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-08 01:59 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | edge | 26.29% | $32,188,576 | $0.3968 |
| 2 | m | 10.91% | $15,187,195 | $1.3600 |
| 3 | ldo | 10.79% | $62,548,784 | $0.3126 |
| 4 | wemix | 7.98% | $2,300,076 | $0.2849 |
| 5 | shfl | 7.60% | $1,036,545 | $0.2807 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | -65.17% | $131,194,005 | $5.0300 |
| 2 | gwei | -26.72% | $9,260,332 | $0.1003 |
| 3 | grass | -24.79% | $43,892,473 | $0.3950 |
| 4 | ansem | -23.12% | $61,829,060 | $0.3147 |
| 5 | xpl | -11.93% | $70,122,058 | $0.0970 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $49,355,742,131 | $0.9993 |
| 2 | btc | -1.31% | $31,804,526,486 | $63,019.0000 |
| 3 | usdc | -0.01% | $12,852,246,948 | $0.9999 |
| 4 | eth | -2.12% | $10,077,283,666 | $1,754.8200 |
| 5 | sol | -3.41% | $2,260,165,450 | $79.1000 |


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
