# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-01 02:54 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | 86.22% | $326,478,496 | $0.6521 |
| 2 | home | 39.14% | $92,624,254 | $0.0396 |
| 3 | koge | 35.44% | $1,190,208 | $47.9800 |
| 4 | 币安人生 | 21.62% | $102,818,484 | $0.6323 |
| 5 | ff | 16.17% | $17,509,498 | $0.1170 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | genius | -14.21% | $55,758,189 | $0.4216 |
| 2 | edge | -10.10% | $9,330,157 | $1.2700 |
| 3 | skyai | -6.69% | $17,014,024 | $0.1690 |
| 4 | bgb | -6.53% | $25,571,495 | $2.0900 |
| 5 | rail | -6.26% | $1,038,102 | $2.8000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $35,961,701,327 | $0.9985 |
| 2 | btc | -0.27% | $17,913,187,831 | $73,705.0000 |
| 3 | eth | -0.91% | $9,454,642,666 | $2,009.3700 |
| 4 | usdc | -0.01% | $7,067,820,257 | $0.9996 |
| 5 | bnb | -4.65% | $2,351,777,005 | $705.1700 |


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
