# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-13 01:07 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ip | 17.28% | $301,609,325 | $2.9200 |
| 2 | b | 15.42% | $24,066,994 | $0.2675 |
| 3 | river | 14.37% | $47,775,449 | $19.7200 |
| 4 | xmr | 10.60% | $502,248,096 | $645.4900 |
| 5 | dash | 6.67% | $104,569,429 | $40.1700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lit | -14.85% | $16,034,355 | $2.1900 |
| 2 | render | -7.83% | $170,958,712 | $2.3800 |
| 3 | ena | -6.94% | $156,524,916 | $0.2149 |
| 4 | pol | -6.92% | $261,370,105 | $0.1518 |
| 5 | xpl | -6.52% | $85,804,683 | $0.1541 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $75,065,873,030 | $0.9989 |
| 2 | btc | -0.09% | $45,775,012,020 | $91,336.0000 |
| 3 | eth | -0.80% | $20,659,189,058 | $3,105.6100 |
| 4 | usdc | -0.01% | $13,524,033,645 | $0.9997 |
| 5 | sol | -1.46% | $6,169,627,131 | $139.1200 |


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
