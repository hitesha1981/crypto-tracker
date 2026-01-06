# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-06 01:10 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xcn | 50.12% | $139,167,819 | $0.0089 |
| 2 | river | 27.97% | $35,131,813 | $16.4700 |
| 3 | wstx | 23.73% | $2,999 | $0.3713 |
| 4 | virtual | 16.14% | $426,215,238 | $1.0750 |
| 5 | sui | 15.00% | $1,749,780,399 | $1.9700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | -31.80% | $53,827,643 | $0.3498 |
| 2 | myx | -20.78% | $43,535,756 | $4.8600 |
| 3 | stable | -8.00% | $35,141,206 | $0.0155 |
| 4 | cc | -7.00% | $33,572,862 | $0.1405 |
| 5 | borg | -6.16% | $891,385 | $0.2672 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $93,528,028,434 | $0.9999 |
| 2 | btc | 1.49% | $55,732,023,257 | $93,838.0000 |
| 3 | eth | 1.60% | $28,037,231,982 | $3,219.1500 |
| 4 | usdc | -0.02% | $15,269,842,963 | $0.9997 |
| 5 | xrp | 12.58% | $7,423,081,693 | $2.3800 |


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
