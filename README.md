# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-30 02:51 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pons | 78.22% | $44,927,957 | $0.2751 |
| 2 | prom | 51.06% | $67,198,358 | $7.5000 |
| 3 | cards | 42.90% | $13,267,622 | $0.2475 |
| 4 | cys | 24.18% | $18,808,359 | $0.7548 |
| 5 | btw | 12.52% | $13,490,396 | $0.4457 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | -27.12% | $43,084,311 | $0.0081 |
| 2 | trump | -6.08% | $626,840,107 | $2.6400 |
| 3 | npc | -5.43% | $2,844,726 | $0.0173 |
| 4 | tibbir | -4.77% | $1,627,758 | $0.2766 |
| 5 | stx | -4.66% | $18,434,490 | $0.2400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $28,003,935,954 | $1.0000 |
| 2 | btc | 0.59% | $14,641,048,540 | $78,095.0000 |
| 3 | usdc | -0.00% | $7,046,119,687 | $1.0000 |
| 4 | eth | 0.71% | $5,380,691,419 | $2,455.3400 |
| 5 | sol | 1.36% | $2,213,681,472 | $105.2400 |


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
