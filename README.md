# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-13 02:00 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | 174.93% | $450,048,087 | $5.7900 |
| 2 | 币安人生 | 41.88% | $112,936,480 | $0.1894 |
| 3 | tibbir | 24.73% | $2,788,854 | $0.1318 |
| 4 | siren | 16.55% | $26,283,466 | $0.8267 |
| 5 | ultima | 14.59% | $20,812,531 | $5,102.4000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | edge | -11.34% | $250,724,453 | $0.8875 |
| 2 | dash | -8.23% | $221,577,085 | $41.6100 |
| 3 | ff | -5.88% | $59,448,070 | $0.0801 |
| 4 | chz | -5.86% | $76,339,079 | $0.0360 |
| 5 | dcr | -5.85% | $1,883,373 | $21.2100 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $46,707,972,323 | $1.0000 |
| 2 | btc | -0.50% | $27,557,484,198 | $71,201.0000 |
| 3 | eth | -0.52% | $13,620,323,440 | $2,203.9600 |
| 4 | usdc | -0.01% | $7,709,403,429 | $0.9999 |
| 5 | sol | -0.00% | $2,726,615,754 | $82.3100 |


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
