# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-16 01:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | vvv | 28.84% | $57,230,215 | $4.1200 |
| 2 | hnt | 16.73% | $18,064,493 | $1.3000 |
| 3 | stable | 16.57% | $31,494,849 | $0.0266 |
| 4 | h | 12.36% | $107,763,873 | $0.2226 |
| 5 | kite | 7.18% | $142,727,586 | $0.2059 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skr | -10.73% | $6,149,415 | $0.0210 |
| 2 | fartcoin | -9.25% | $46,550,030 | $0.1976 |
| 3 | aero | -9.14% | $13,773,179 | $0.3072 |
| 4 | pengu | -9.10% | $136,329,942 | $0.0071 |
| 5 | river | -9.09% | $22,003,009 | $12.5100 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $85,834,196,579 | $0.9996 |
| 2 | btc | -1.22% | $44,171,783,900 | $68,694.0000 |
| 3 | eth | -4.79% | $32,334,227,114 | $1,966.7200 |
| 4 | usdc | 0.01% | $10,132,408,646 | $1.0000 |
| 5 | xrp | -3.58% | $5,385,569,433 | $1.4700 |


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
