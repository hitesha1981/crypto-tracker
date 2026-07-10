# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-10 02:12 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | 21.35% | $10,060,548 | $0.4900 |
| 2 | tibbir | 20.73% | $1,490,367 | $0.1197 |
| 3 | dexe | 20.07% | $74,136,000 | $34.4500 |
| 4 | sent | 19.45% | $506,874,777 | $0.0164 |
| 5 | cashcat | 19.34% | $41,497,512 | $0.1143 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | -19.22% | $211,547,416 | $1.1200 |
| 2 | hash | -9.76% | $13,311 | $0.0083 |
| 3 | m | -8.52% | $13,536,462 | $1.2200 |
| 4 | gwei | -8.10% | $6,217,894 | $0.0796 |
| 5 | nex | -8.10% | $25,720,471 | $0.0000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $40,895,345,830 | $0.9991 |
| 2 | btc | 2.81% | $27,381,790,833 | $63,753.0000 |
| 3 | usdc | -0.01% | $11,378,108,130 | $0.9998 |
| 4 | eth | 1.66% | $7,847,073,530 | $1,765.3500 |
| 5 | sol | 1.58% | $1,622,204,297 | $78.8500 |


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
