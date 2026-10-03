# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-03 03:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sand | 62.91% | $774,681,925 | $0.0731 |
| 2 | grx | 62.15% | $2,702,566 | $21.1700 |
| 3 | cards | 38.54% | $33,558,546 | $0.2834 |
| 4 | night | 28.10% | $115,656,837 | $0.0499 |
| 5 | mana | 16.46% | $166,631,766 | $0.1032 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ai | -22.99% | $16,047,388 | $0.1373 |
| 2 | 2z | -20.48% | $34,968,442 | $0.0452 |
| 3 | rain | -17.94% | $15,276,077 | $0.0099 |
| 4 | pons | -17.25% | $43,079,144 | $0.4234 |
| 5 | prl | -14.96% | $4,451,502 | $1.0040 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $78,734,943,789 | $0.9999 |
| 2 | btc | -0.78% | $43,700,144,415 | $84,563.0000 |
| 3 | usdc | 0.01% | $22,612,672,666 | $1.0000 |
| 4 | eth | -1.51% | $18,319,875,494 | $2,677.2900 |
| 5 | sol | -0.91% | $4,480,670,778 | $118.9100 |


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
