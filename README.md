# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-15 02:31 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hype | 17.52% | $668,851,247 | $45.7300 |
| 2 | gwei | 14.85% | $7,054,979 | $0.1498 |
| 3 | troll | 14.10% | $19,473,757 | $0.1367 |
| 4 | ub | 13.77% | $38,971,483 | $0.2327 |
| 5 | tel | 13.47% | $5,779,022 | $0.0032 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -51.52% | $106,328,188 | $0.5567 |
| 2 | b | -28.27% | $81,721,895 | $0.4701 |
| 3 | skyai | -17.15% | $55,625,633 | $0.3909 |
| 4 | ff | -7.59% | $53,608,480 | $0.0804 |
| 5 | icp | -7.15% | $120,508,239 | $2.8300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $73,337,466,909 | $0.9997 |
| 2 | btc | 1.61% | $45,255,232,238 | $80,885.0000 |
| 3 | eth | 0.11% | $17,198,745,503 | $2,263.9600 |
| 4 | usdc | -0.00% | $15,976,050,387 | $0.9997 |
| 5 | xrp | 3.22% | $3,815,848,104 | $1.4800 |


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
