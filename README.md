# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-17 01:55 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ordi | 148.58% | $1,426,732,986 | $8.9700 |
| 2 | siren | 84.10% | $110,522,449 | $1.5300 |
| 3 | rave | 54.21% | $300,236,643 | $17.0300 |
| 4 | ip | 35.01% | $183,463,935 | $0.6795 |
| 5 | m | 32.14% | $25,675,601 | $3.7600 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | enj | -16.72% | $454,375,370 | $0.0777 |
| 2 | dexe | -6.79% | $17,141,323 | $11.2200 |
| 3 | morpho | -5.47% | $21,852,534 | $1.7800 |
| 4 | mon | -5.17% | $109,995,186 | $0.0340 |
| 5 | hash | -4.56% | $8,495 | $0.0116 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $79,864,732,635 | $1.0000 |
| 2 | btc | -0.02% | $43,627,321,643 | $74,613.0000 |
| 3 | eth | -0.94% | $20,443,042,311 | $2,329.4500 |
| 4 | usdc | -0.01% | $18,725,964,408 | $0.9999 |
| 5 | sol | 3.73% | $5,486,847,433 | $88.0000 |


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
