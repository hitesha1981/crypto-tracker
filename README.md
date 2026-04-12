# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-12 01:55 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skyai | 53.75% | $59,676,159 | $0.1128 |
| 2 | gwei | 36.69% | $23,769,623 | $0.0695 |
| 3 | aria | 28.30% | $55,480,625 | $0.7673 |
| 4 | 币安人生 | 15.89% | $84,053,437 | $0.1335 |
| 5 | rave | 13.19% | $210,434,191 | $2.1000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ff | -12.75% | $152,423,636 | $0.0854 |
| 2 | shfl | -8.90% | $708,918 | $0.2926 |
| 3 | h | -8.76% | $25,179,558 | $0.0940 |
| 4 | kau | -8.19% | $7,736 | $155.8200 |
| 5 | spx | -7.48% | $6,356,059 | $0.3095 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $44,624,061,501 | $1.0000 |
| 2 | btc | -1.84% | $25,975,493,933 | $71,614.0000 |
| 3 | eth | -1.18% | $13,158,676,517 | $2,218.6600 |
| 4 | usdc | 0.01% | $6,868,767,371 | $1.0000 |
| 5 | sol | -2.68% | $2,545,089,122 | $82.3800 |


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
