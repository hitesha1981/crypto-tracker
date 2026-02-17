# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-17 01:25 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | 57.29% | $32,424,272 | $0.2261 |
| 2 | stable | 18.58% | $60,842,645 | $0.0315 |
| 3 | kmno | 11.60% | $7,850,338 | $0.0336 |
| 4 | m | 9.99% | $8,695,505 | $1.4300 |
| 5 | hnt | 9.53% | $29,545,715 | $1.4200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -12.44% | $34,679,210 | $0.1950 |
| 2 | myx | -10.70% | $17,658,570 | $1.8700 |
| 3 | tibbir | -8.26% | $6,203,921 | $0.1305 |
| 4 | pippin | -7.64% | $51,428,925 | $0.6443 |
| 5 | pi | -5.89% | $27,976,482 | $0.1734 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $62,347,851,256 | $0.9997 |
| 2 | btc | 0.31% | $36,379,571,994 | $68,906.0000 |
| 3 | eth | 1.82% | $16,858,298,367 | $2,002.5100 |
| 4 | sol | 0.91% | $3,651,914,162 | $86.9100 |
| 5 | usdc | -0.00% | $3,239,912,083 | $0.9999 |


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
