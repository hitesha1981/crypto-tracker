# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-05 02:43 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | home | 46.66% | $121,283,465 | $0.0560 |
| 2 | siren | 24.21% | $65,609,924 | $0.7305 |
| 3 | beat | 18.59% | $37,639,503 | $1.5600 |
| 4 | koge | 16.33% | $970,882 | $63.5100 |
| 5 | dexe | 15.08% | $30,079,090 | $20.8300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zec | -33.08% | $1,483,916,267 | $398.6000 |
| 2 | lab | -32.07% | $96,047,784 | $11.5400 |
| 3 | near | -20.57% | $1,122,751,611 | $2.1900 |
| 4 | grass | -20.35% | $41,143,988 | $0.3547 |
| 5 | vvv | -17.62% | $92,615,247 | $16.2200 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $93,076,221,727 | $0.9989 |
| 2 | btc | -0.98% | $54,575,209,994 | $62,696.0000 |
| 3 | eth | -2.17% | $23,150,887,208 | $1,733.5200 |
| 4 | usdc | 0.01% | $21,930,659,357 | $0.9997 |
| 5 | sol | -2.95% | $4,283,955,883 | $67.8600 |


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
