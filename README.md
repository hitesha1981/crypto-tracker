# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-10 01:09 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | tut | 67.00% | $665,023,867 | $0.1900 |
| 2 | m | 66.70% | $383,597 | $1.2900 |
| 3 | tibbir | 18.40% | $2,342,569 | $0.1173 |
| 4 | pump | 14.40% | $145,164,517 | $0.0028 |
| 5 | cashcat | 8.70% | $20,203,460 | $0.1328 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | peanut | -14.90% | $2 | $0.0006 |
| 2 | us | -11.60% | $22,314,609 | $0.0438 |
| 3 | fgrs | -10.10% | $26,008 | $26.0100 |
| 4 | strk | -6.80% | $10,172,326 | $0.0234 |
| 5 | tel | -6.60% | $1,208,090 | $0.0016 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $22,528,371,697 | $0.9994 |
| 2 | btc | 0.00% | $13,357,844,794 | $64,887.0000 |
| 3 | usdc | 0.00% | $4,973,645,330 | $0.9997 |
| 4 | eth | -0.20% | $4,264,364,441 | $1,908.6100 |
| 5 | sol | 0.70% | $1,133,592,037 | $76.4500 |


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
