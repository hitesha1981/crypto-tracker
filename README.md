# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-13 02:03 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ansem | 31.18% | $36,663,060 | $0.2682 |
| 2 | dexe | 27.10% | $148,775,580 | $48.5000 |
| 3 | velvet | 23.11% | $18,750,837 | $0.5260 |
| 4 | bill | 19.30% | $25,205,229 | $0.0507 |
| 5 | dcr | 15.85% | $6,661,145 | $12.9300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | -23.25% | $75,923,792 | $0.4187 |
| 2 | cashcat | -23.03% | $50,846,109 | $0.1668 |
| 3 | gwei | -14.78% | $7,833,294 | $0.0552 |
| 4 | pi | -9.42% | $11,860,964 | $0.0885 |
| 5 | tibbir | -8.46% | $1,012,951 | $0.1198 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $29,295,030,316 | $0.9993 |
| 2 | btc | -1.13% | $19,102,408,228 | $63,316.0000 |
| 3 | eth | 0.04% | $6,268,927,366 | $1,803.7800 |
| 4 | usdc | -0.01% | $6,227,003,107 | $0.9997 |
| 5 | sol | -0.62% | $1,262,641,943 | $76.2800 |


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
