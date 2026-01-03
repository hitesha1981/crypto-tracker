# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-03 01:06 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stable | 28.32% | $56,906,199 | $0.0189 |
| 2 | pepe | 25.27% | $1,857,213,744 | $0.0000 |
| 3 | hash | 22.16% | $18,883 | $0.0327 |
| 4 | fluid | 20.99% | $10,274,242 | $3.2400 |
| 5 | river | 19.56% | $30,002,036 | $18.2700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | merl | -6.75% | $31,423,054 | $0.2653 |
| 2 | h | -6.74% | $46,320,191 | $0.1660 |
| 3 | zec | -6.37% | $609,689,593 | $493.6400 |
| 4 | pippin | -4.94% | $27,185,244 | $0.3748 |
| 5 | cc | -4.41% | $36,392,527 | $0.1479 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.07% | $84,568,864,169 | $0.9996 |
| 2 | btc | 1.65% | $50,302,038,912 | $90,126.0000 |
| 3 | eth | 4.28% | $25,770,007,645 | $3,129.0700 |
| 4 | usdc | -0.01% | $13,874,574,361 | $0.9998 |
| 5 | sol | 4.63% | $4,892,544,101 | $132.4500 |


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
