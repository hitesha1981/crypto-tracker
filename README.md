# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-27 01:06 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | 33.43% | $69,683,553 | $2.0200 |
| 2 | dcr | 21.98% | $25,023,825 | $18.8400 |
| 3 | tel | 15.49% | $8,024,560 | $0.0044 |
| 4 | m | 10.32% | $15,997,114 | $1.4500 |
| 5 | rain | 10.29% | $51,752,450 | $0.0077 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sky | -9.19% | $21,381,521 | $0.0612 |
| 2 | hash | -7.13% | $45,475 | $0.0305 |
| 3 | vsn | -5.95% | $15,702,228 | $0.0796 |
| 4 | h | -5.68% | $52,499,446 | $0.1533 |
| 5 | merl | -5.08% | $18,401,400 | $0.4278 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $70,933,472,450 | $0.9994 |
| 2 | btc | 0.11% | $45,627,573,787 | $87,299.0000 |
| 3 | eth | 0.65% | $18,089,918,673 | $2,924.3800 |
| 4 | usdc | -0.00% | $9,744,917,948 | $0.9997 |
| 5 | sol | 1.47% | $4,028,867,793 | $121.9600 |


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
