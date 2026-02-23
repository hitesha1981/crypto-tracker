# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-23 01:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | 23.87% | $58,751,531 | $0.6214 |
| 2 | kite | 17.37% | $196,145,624 | $0.2575 |
| 3 | dexe | 7.52% | $5,809,287 | $2.5800 |
| 4 | siren | 6.38% | $11,488,405 | $0.2865 |
| 5 | rave | 4.61% | $72,438,062 | $0.6814 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | myx | -31.96% | $31,752,478 | $0.6810 |
| 2 | vvv | -15.70% | $11,527,057 | $3.7500 |
| 3 | xpl | -12.63% | $44,049,028 | $0.0832 |
| 4 | tibbir | -12.08% | $7,794,705 | $0.1562 |
| 5 | fartcoin | -11.86% | $35,033,625 | $0.1601 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $41,314,591,828 | $0.9998 |
| 2 | btc | -4.47% | $25,034,600,993 | $65,033.0000 |
| 3 | eth | -5.32% | $16,370,634,776 | $1,871.1500 |
| 4 | sol | -7.80% | $2,529,937,637 | $78.5400 |
| 5 | usdc | 0.00% | $2,521,991,298 | $1.0000 |


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
