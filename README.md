# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-07 01:20 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skr | 24.81% | $73,951,217 | $0.0272 |
| 2 | night | 24.56% | $26,501,471 | $0.0541 |
| 3 | awe | 22.98% | $50,873,170 | $0.0754 |
| 4 | xdc | 22.23% | $43,273,808 | $0.0370 |
| 5 | leo | 19.10% | $2,634,945 | $8.1900 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | apepe | -15.64% | $11,357,565 | $0.0000 |
| 2 | stable | -10.78% | $44,446,029 | $0.0178 |
| 3 | hype | -6.18% | $926,944,763 | $31.8000 |
| 4 | zano | -5.51% | $2,112,427 | $8.4400 |
| 5 | wlfi | -5.00% | $365,668,938 | $0.1062 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.10% | $183,927,070,170 | $0.9996 |
| 2 | btc | 9.18% | $111,120,561,843 | $69,931.0000 |
| 3 | eth | 7.97% | $56,810,153,513 | $2,040.6200 |
| 4 | usdc | 0.01% | $12,795,692,101 | $0.9999 |
| 5 | xrp | 16.67% | $11,706,755,401 | $1.4400 |


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
