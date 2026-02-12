# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-12 01:28 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bera | 80.19% | $928,394,524 | $0.9180 |
| 2 | pippin | 31.10% | $57,310,510 | $0.5121 |
| 3 | s | 21.85% | $51,983,269 | $0.0494 |
| 4 | 0g | 9.08% | $25,581,546 | $0.5838 |
| 5 | jasmy | 8.57% | $31,732,976 | $0.0059 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | myx | -46.08% | $48,461,579 | $3.0000 |
| 2 | kite | -16.50% | $60,810,632 | $0.1633 |
| 3 | hash | -11.46% | $30,666 | $0.0178 |
| 4 | satusd | -9.15% | $9 | $0.9041 |
| 5 | uds | -8.83% | $397,794 | $1.8000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $86,631,516,013 | $0.9994 |
| 2 | btc | -1.70% | $55,548,393,955 | $67,753.0000 |
| 3 | eth | -2.39% | $24,966,323,384 | $1,969.4200 |
| 4 | usdc | 0.01% | $15,310,612,947 | $0.9999 |
| 5 | sol | -3.66% | $3,975,863,557 | $80.2300 |


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
