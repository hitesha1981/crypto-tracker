# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-26 00:51 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | meta | 28.87% | $59,792,038 | $7.8600 |
| 2 | rain | 23.70% | $49,162,540 | $0.0182 |
| 3 | stx | 14.31% | $106,515,301 | $0.2687 |
| 4 | ff | 12.00% | $28,975,253 | $0.1010 |
| 5 | spx | 11.35% | $25,176,880 | $0.5152 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kag | -24.74% | $3,658 | $47.0300 |
| 2 | cashcat | -18.12% | $53,197,241 | $0.1829 |
| 3 | mon | -12.61% | $63,547,836 | $0.0278 |
| 4 | zama | -11.43% | $12,650,803 | $0.0537 |
| 5 | met | -10.54% | $9,140,930 | $0.2126 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $68,698,793,568 | $0.9999 |
| 2 | btc | -1.32% | $42,152,530,029 | $78,518.0000 |
| 3 | usdc | 0.00% | $19,261,566,814 | $0.9999 |
| 4 | eth | -1.94% | $15,031,326,674 | $2,444.4100 |
| 5 | sol | -4.93% | $5,235,451,254 | $96.6100 |


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
