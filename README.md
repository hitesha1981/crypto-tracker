# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-15 01:51 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | om | 352.32% | $6,482 | $0.0669 |
| 2 | rave | 125.01% | $464,911,500 | $19.2800 |
| 3 | 币安人生 | 64.20% | $338,028,065 | $0.3510 |
| 4 | enj | 36.17% | $424,628,274 | $0.0617 |
| 5 | genius | 19.96% | $33,819,916 | $0.6470 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ultima | -17.58% | $14,468,989 | $4,286.3100 |
| 2 | hash | -10.56% | $43,824 | $0.0110 |
| 3 | siren | -10.27% | $21,491,380 | $0.7014 |
| 4 | tibbir | -8.88% | $2,262,304 | $0.1364 |
| 5 | night | -7.86% | $43,363,572 | $0.0359 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $89,215,624,615 | $1.0000 |
| 2 | btc | 0.35% | $55,758,224,279 | $74,680.0000 |
| 3 | eth | -1.36% | $24,038,931,843 | $2,340.1300 |
| 4 | usdc | -0.01% | $22,021,473,422 | $0.9998 |
| 5 | sol | -2.53% | $4,586,601,437 | $83.9200 |


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
