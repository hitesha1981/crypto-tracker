# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-28 02:31 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rain | 25.36% | $45,346,387 | $0.0145 |
| 2 | xlm | 20.34% | $726,228,004 | $0.1776 |
| 3 | ff | 9.50% | $74,361,480 | $0.1023 |
| 4 | beat | 8.91% | $27,234,172 | $1.1700 |
| 5 | jto | 6.91% | $75,023,803 | $0.5496 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skyai | -15.44% | $33,348,321 | $0.1800 |
| 2 | h | -14.80% | $110,961,189 | $0.2135 |
| 3 | pendle | -13.49% | $55,904,438 | $1.5500 |
| 4 | render | -10.16% | $141,716,411 | $2.0600 |
| 5 | wld | -8.20% | $262,836,471 | $0.3302 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $61,385,081,419 | $0.9984 |
| 2 | btc | -2.07% | $36,845,468,453 | $74,101.0000 |
| 3 | usdc | -0.02% | $15,569,166,072 | $0.9996 |
| 4 | eth | -2.64% | $13,747,033,367 | $2,014.4700 |
| 5 | sol | -1.85% | $2,662,883,641 | $82.0600 |


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
