# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-24 02:36 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rail | 39.46% | $4,639,993 | $3.3500 |
| 2 | grass | 35.76% | $53,653,659 | $0.5449 |
| 3 | ub | 22.76% | $26,740,449 | $0.1383 |
| 4 | bsb | 18.68% | $98,211,221 | $1.2400 |
| 5 | beat | 12.99% | $45,084,235 | $1.4900 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | -10.15% | $25,347,991 | $4.3300 |
| 2 | xp | -8.85% | $1,637,691 | $0.0494 |
| 3 | chz | -6.78% | $129,420,689 | $0.0380 |
| 4 | hash | -6.51% | $18,133 | $0.0108 |
| 5 | btse | -5.22% | $4,740,753 | $1.0630 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $53,126,350,136 | $0.9987 |
| 2 | btc | 1.74% | $30,751,916,921 | $76,714.0000 |
| 3 | eth | 2.64% | $16,001,801,453 | $2,118.1200 |
| 4 | usdc | -0.01% | $9,835,909,739 | $0.9997 |
| 5 | sol | 1.74% | $3,188,942,868 | $85.7000 |


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
