# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-14 02:44 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 26.87% | $43,300,643 | $0.6952 |
| 2 | lsk | 24.84% | $361,337,853 | $0.8378 |
| 3 | fil | 24.00% | $338,252,863 | $1.0010 |
| 4 | ar | 12.58% | $22,698,823 | $2.8800 |
| 5 | h | 10.56% | $4,387,315 | $0.0868 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stonk | -25.32% | $53,059,264 | $0.2092 |
| 2 | ai | -17.84% | $24,189,722 | $0.2455 |
| 3 | uai | -14.92% | $20,107,173 | $0.5052 |
| 4 | 牛来 | -14.01% | $61,288,994 | $0.1191 |
| 5 | mina | -13.74% | $16,792,134 | $0.0899 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $36,606,611,655 | $0.9997 |
| 2 | btc | 0.25% | $17,917,556,331 | $77,418.0000 |
| 3 | eth | -0.80% | $10,423,893,877 | $2,500.4900 |
| 4 | usdc | -0.01% | $8,354,724,939 | $0.9998 |
| 5 | sol | -1.24% | $2,197,788,093 | $100.6100 |


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
