# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-20 05:08 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | icnt | 28.42% | $31,052,813 | $0.4340 |
| 2 | meta | 27.52% | $19,795,354 | $4.3100 |
| 3 | btw | 9.52% | $10,648,235 | $0.6177 |
| 4 | cap | 6.38% | $13,678,312 | $0.0959 |
| 5 | pieverse | 3.35% | $186,124,093 | $3.0100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pearl | -17.52% | $34,742,240 | $1.9300 |
| 2 | bp | -14.61% | $4,621,864 | $0.8282 |
| 3 | jup | -13.93% | $53,602,097 | $0.2292 |
| 4 | sent | -13.19% | $42,823,629 | $0.0201 |
| 5 | near | -11.86% | $524,124,268 | $3.0100 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $51,003,437,670 | $0.9992 |
| 2 | btc | -3.24% | $34,714,122,297 | $61,435.0000 |
| 3 | usdc | 0.00% | $14,833,132,102 | $0.9996 |
| 4 | eth | -4.20% | $11,793,722,562 | $1,722.5200 |
| 5 | u | 0.03% | $2,522,273,755 | $0.9993 |


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
