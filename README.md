# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-24 01:59 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bcap | 363.10% | $0 | $106.2000 |
| 2 | m | 66.70% | $383,597 | $1.2900 |
| 3 | bank | 24.60% | $144,066,374 | $0.2748 |
| 4 | beat | 16.30% | $15,139,709 | $3.0700 |
| 5 | zbt | 11.80% | $16,630,536 | $0.1156 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | grok | -100.00% | $25 | $0.0000 |
| 2 | dexe | -61.40% | $141,588,892 | $1.9400 |
| 3 | earneth | -58.90% | $0 | $1,901.7700 |
| 4 | velvet | -33.10% | $5,998,091 | $0.3047 |
| 5 | b | -25.10% | $13,824,800 | $0.1690 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $39,765,483,226 | $0.9993 |
| 2 | btc | -1.70% | $24,668,454,489 | $65,033.0000 |
| 3 | usdc | 0.00% | $10,749,161,874 | $0.9997 |
| 4 | eth | -3.30% | $9,481,345,629 | $1,872.3900 |
| 5 | sol | -2.90% | $1,546,161,701 | $75.6400 |


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
