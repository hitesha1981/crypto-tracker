# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-20 02:37 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bsb | 20.68% | $86,032,685 | $0.8197 |
| 2 | lit | 17.04% | $52,359,744 | $1.1600 |
| 3 | 9bit | 13.20% | $10,678,326 | $0.0386 |
| 4 | xp | 10.74% | $3,023,222 | $0.0533 |
| 5 | vvv | 10.13% | $101,006,033 | $16.3300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bill | -17.60% | $115,042,406 | $0.1104 |
| 2 | pieverse | -15.59% | $11,572,886 | $0.7180 |
| 3 | skyai | -12.38% | $35,380,659 | $0.2781 |
| 4 | mbtc | -10.14% | $23,485 | $0.1691 |
| 5 | lab | -9.54% | $138,362,785 | $4.3000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $47,209,848,783 | $0.9990 |
| 2 | btc | -0.17% | $27,788,194,648 | $76,600.0000 |
| 3 | usdc | -0.00% | $12,136,365,204 | $0.9997 |
| 4 | eth | -0.90% | $11,809,665,572 | $2,107.1800 |
| 5 | sol | -1.05% | $1,971,304,599 | $84.0900 |


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
