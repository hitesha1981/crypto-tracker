# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-01 01:56 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | qrl | 51.65% | $613,576 | $1.7200 |
| 2 | edge | 23.51% | $177,123,525 | $0.6491 |
| 3 | algo | 19.37% | $93,545,579 | $0.0993 |
| 4 | stable | 14.31% | $45,810,931 | $0.0278 |
| 5 | ray | 14.03% | $102,657,687 | $0.6522 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -78.27% | $142,108,024 | $0.3644 |
| 2 | twt | -14.97% | $58,330,850 | $0.3618 |
| 3 | kite | -8.85% | $62,609,931 | $0.1514 |
| 4 | river | -7.23% | $22,546,297 | $16.1400 |
| 5 | xcn | -6.31% | $6,392,084 | $0.0048 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $83,073,279,729 | $0.9992 |
| 2 | btc | -0.13% | $57,122,871,463 | $67,844.0000 |
| 3 | eth | 1.02% | $20,583,673,044 | $2,093.9100 |
| 4 | usdc | 0.00% | $8,777,858,904 | $0.9997 |
| 5 | sol | -1.13% | $4,237,849,910 | $82.8500 |


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
