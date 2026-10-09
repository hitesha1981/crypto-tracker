# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-09 03:56 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hash | 37.20% | $38,676 | $0.0075 |
| 2 | strk | 32.37% | $335,751,230 | $0.0654 |
| 3 | drv | 25.99% | $71,116,962 | $0.4579 |
| 4 | soso | 13.56% | $5,917,949 | $0.3680 |
| 5 | pyth | 11.78% | $106,045,621 | $0.0809 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pons | -15.27% | $106,590,624 | $0.3613 |
| 2 | crv | -12.73% | $114,455,306 | $0.3435 |
| 3 | cvx | -12.31% | $12,987,948 | $2.0300 |
| 4 | edge | -11.15% | $4,663,072 | $0.3647 |
| 5 | near | -10.93% | $1,714,173,193 | $4.7600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $79,997,536,624 | $0.9993 |
| 2 | btc | -0.47% | $42,611,204,830 | $82,319.0000 |
| 3 | usdc | -0.00% | $24,453,481,085 | $0.9996 |
| 4 | eth | -2.97% | $19,087,863,512 | $2,489.6500 |
| 5 | sol | -4.75% | $5,208,332,483 | $110.2300 |


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
