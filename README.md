# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-03 02:23 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | 70.78% | $92,318,485 | $0.0151 |
| 2 | egld | 23.52% | $45,216,769 | $5.0300 |
| 3 | pons | 22.22% | $135,679,549 | $0.5146 |
| 4 | useless | 18.89% | $63,508,692 | $0.1292 |
| 5 | cashcat | 18.06% | $86,968,253 | $0.2780 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cards | -11.56% | $3,828,890 | $0.1580 |
| 2 | pwt | -8.44% | $2,740,799 | $0.5200 |
| 3 | hash | -7.01% | $6,778 | $0.0075 |
| 4 | sky | -6.94% | $9,926,824 | $0.0678 |
| 5 | cvx | -6.50% | $5,846,076 | $2.2300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $47,019,142,912 | $0.9997 |
| 2 | btc | 0.32% | $26,279,667,233 | $77,432.0000 |
| 3 | usdc | 0.00% | $12,954,217,420 | $0.9998 |
| 4 | eth | -0.63% | $12,431,281,682 | $2,389.5900 |
| 5 | sol | 1.04% | $2,886,913,000 | $100.2800 |


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
