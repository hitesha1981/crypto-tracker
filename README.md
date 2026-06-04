# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-04 02:55 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | wld | 33.07% | $1,001,519,224 | $0.5225 |
| 2 | beat | 23.12% | $25,122,046 | $1.3600 |
| 3 | tel | 17.92% | $3,095,828 | $0.0028 |
| 4 | ena | 17.38% | $670,683,924 | $0.1071 |
| 5 | rail | 16.05% | $2,209,343 | $2.4900 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | jst | -23.14% | $113,049,891 | $0.0722 |
| 2 | home | -22.28% | $29,499,038 | $0.0382 |
| 3 | dexe | -18.50% | $42,772,572 | $18.0300 |
| 4 | h | -18.38% | $153,482,092 | $0.5516 |
| 5 | ub | -17.73% | $24,635,778 | $0.1033 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $328,096,843,746 | $0.9989 |
| 2 | btc | -4.99% | $58,225,061,112 | $63,219.0000 |
| 3 | eth | -4.47% | $26,152,646,737 | $1,768.9200 |
| 4 | usdc | 0.02% | $21,434,127,518 | $0.9998 |
| 5 | sol | -5.48% | $4,767,634,631 | $70.2200 |


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
