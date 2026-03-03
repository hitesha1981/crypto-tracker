# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-03 01:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | 73.73% | $41,857,162 | $0.4408 |
| 2 | robo | 36.68% | $97,656,232 | $0.0525 |
| 3 | cheems | 20.57% | $1,832,764 | $0.0000 |
| 4 | near | 18.78% | $710,255,339 | $1.3900 |
| 5 | tibbir | 14.92% | $8,714,977 | $0.1773 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kite | -17.13% | $132,582,267 | $0.2125 |
| 2 | pol | -5.99% | $103,392,123 | $0.1011 |
| 3 | borg | -5.06% | $514,558 | $0.1901 |
| 4 | stable | -4.76% | $29,805,107 | $0.0312 |
| 5 | dot | -4.33% | $263,805,180 | $1.5100 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $96,898,180,679 | $1.0000 |
| 2 | btc | 3.55% | $59,950,431,140 | $69,010.0000 |
| 3 | eth | 3.23% | $26,688,403,603 | $2,034.6600 |
| 4 | usdc | -0.01% | $7,191,261,424 | $0.9999 |
| 5 | sol | 1.83% | $5,906,257,954 | $86.7800 |


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
