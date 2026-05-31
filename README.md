# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-31 02:46 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | 28.33% | $131,419,518 | $0.3606 |
| 2 | lab | 27.78% | $139,433,982 | $8.5800 |
| 3 | 币安人生 | 16.43% | $56,329,420 | $0.5183 |
| 4 | wld | 14.71% | $447,237,293 | $0.3423 |
| 5 | bgb | 12.81% | $32,559,854 | $2.2400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skyai | -14.99% | $59,678,955 | $0.1816 |
| 2 | xlm | -14.20% | $1,741,976,994 | $0.2401 |
| 3 | rail | -12.43% | $804,756 | $2.9800 |
| 4 | xmr | -11.35% | $209,408,063 | $370.6200 |
| 5 | iota | -10.75% | $18,071,657 | $0.0627 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $35,557,896,526 | $0.9985 |
| 2 | btc | 0.31% | $18,043,494,744 | $73,859.0000 |
| 3 | eth | 0.48% | $6,739,721,979 | $2,027.1400 |
| 4 | usdc | 0.05% | $6,630,675,073 | $1.0000 |
| 5 | bnb | 12.25% | $3,250,276,422 | $736.4600 |


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
