# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-01 03:39 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lit | 15.35% | $94,515,897 | $3.1800 |
| 2 | zro | 11.17% | $152,619,596 | $1.8800 |
| 3 | bat | 9.61% | $19,667,240 | $0.1420 |
| 4 | gomining | 8.82% | $3,373,083 | $0.4094 |
| 5 | morpho | 8.62% | $40,818,060 | $2.3200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | -22.31% | $54,546,340 | $0.0091 |
| 2 | hash | -16.31% | $1,790 | $0.0063 |
| 3 | shfl | -7.25% | $1,255,826 | $0.4201 |
| 4 | btw | -6.28% | $5,332,607 | $1.1300 |
| 5 | m | -6.09% | $937,964 | $0.8975 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btc | 0.63% | $35,885,721,756 | $77,708.0000 |
| 2 | usdt | 0.03% | $25,504,171,868 | $0.9995 |
| 3 | xaut | -0.07% | $22,911,136,870 | $3,875.0800 |
| 4 | usdc | 0.02% | $5,839,621,048 | $1.0000 |
| 5 | eth | 1.23% | $4,356,239,749 | $2,267.2000 |


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
