# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-29 01:14 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cc | 22.19% | $46,360,494 | $0.1389 |
| 2 | uds | 8.31% | $1,147,285 | $2.4400 |
| 3 | borg | 4.74% | $841,050 | $0.2765 |
| 4 | ohm | 4.58% | $593,642 | $22.0000 |
| 5 | h | 4.49% | $47,662,796 | $0.1633 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | -10.84% | $22,783,448 | $0.4211 |
| 2 | dcr | -5.69% | $6,172,597 | $19.0300 |
| 3 | merl | -4.02% | $23,379,286 | $0.3526 |
| 4 | comp | -3.82% | $14,200,008 | $25.9100 |
| 5 | bdx | -3.80% | $11,013,068 | $0.0955 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $35,451,004,992 | $0.9993 |
| 2 | btc | 0.24% | $18,247,176,548 | $88,004.0000 |
| 3 | eth | 0.55% | $9,218,813,373 | $2,960.6500 |
| 4 | usdc | -0.21% | $5,058,353,674 | $1.0000 |
| 5 | sol | 1.68% | $2,699,816,969 | $126.4900 |


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
