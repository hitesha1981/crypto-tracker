# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-10 02:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stonk | 28.25% | $109,529,088 | $0.1941 |
| 2 | apepe | 21.93% | $9,890,745 | $0.0000 |
| 3 | mina | 9.56% | $31,382,000 | $0.0906 |
| 4 | near | 6.17% | $704,615,468 | $2.4300 |
| 5 | btt | 5.05% | $11,061,781 | $0.0000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | useless | -24.35% | $122,574,504 | $0.2210 |
| 2 | ai | -21.20% | $31,615,210 | $0.1927 |
| 3 | pons | -16.04% | $139,158,987 | $0.6360 |
| 4 | fartcoin | -13.47% | $36,411,223 | $0.1427 |
| 5 | xpl | -13.20% | $63,836,575 | $0.0869 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $56,296,776,709 | $0.9997 |
| 2 | btc | -0.98% | $35,284,896,925 | $77,991.0000 |
| 3 | usdc | -0.01% | $16,049,198,425 | $0.9998 |
| 4 | eth | -1.37% | $13,633,618,340 | $2,459.9400 |
| 5 | link | -5.68% | $6,999,724,975 | $11.7500 |


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
