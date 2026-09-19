# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-19 02:32 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | 103.85% | $129,321,363 | $0.0440 |
| 2 | drv | 74.80% | $152,744,963 | $0.4225 |
| 3 | strk | 42.90% | $250,227,290 | $0.0418 |
| 4 | ar | 39.19% | $80,052,248 | $3.8200 |
| 5 | pieverse | 34.89% | $65,213,394 | $1.6200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | geod | -21.18% | $10,868,836 | $0.2686 |
| 2 | btw | -11.02% | $6,906,566 | $0.6279 |
| 3 | edge | -7.63% | $3,308,692 | $0.5831 |
| 4 | h | -5.79% | $4,286,299 | $0.0822 |
| 5 | ai | -5.44% | $23,976,993 | $0.3164 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.05% | $86,353,937,983 | $0.9997 |
| 2 | btc | 5.75% | $45,702,637,639 | $81,329.0000 |
| 3 | eth | 6.36% | $23,991,939,929 | $2,617.7600 |
| 4 | usdc | 0.02% | $23,319,331,655 | $0.9998 |
| 5 | sol | 10.52% | $6,705,331,237 | $113.4200 |


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
