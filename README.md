# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-19 00:47 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 22.30% | $30,887,460 | $0.4448 |
| 2 | tibbir | 20.90% | $2,792,124 | $0.2118 |
| 3 | velvet | 13.90% | $31,736,461 | $0.6580 |
| 4 | gps | 13.10% | $61,707,208 | $0.0187 |
| 5 | pump | 13.00% | $91,890,321 | $0.0031 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dcr | -18.00% | $5,468,093 | $10.3500 |
| 2 | ansem | -16.40% | $15,439,349 | $0.2323 |
| 3 | btse | -7.80% | $8,558,081 | $0.8784 |
| 4 | wld | -6.70% | $157,861,285 | $0.3166 |
| 5 | jasmy | -6.50% | $7,028,565 | $0.0035 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $29,870,473,353 | $0.9994 |
| 2 | btc | 0.70% | $18,078,668,365 | $64,517.0000 |
| 3 | usdc | 0.00% | $7,878,113,273 | $0.9998 |
| 4 | eth | 0.70% | $6,076,302,087 | $1,913.2100 |
| 5 | sol | 1.80% | $1,419,247,510 | $76.9200 |


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
