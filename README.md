# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-16 01:48 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | qubic | 14.91% | $3,553,082 | $0.0000 |
| 2 | ban | 14.30% | $10,559,192 | $0.1342 |
| 3 | xcn | 13.80% | $43,097,238 | $0.0063 |
| 4 | cfx | 11.17% | $63,675,126 | $0.0624 |
| 5 | zro | 9.99% | $80,769,726 | $2.1600 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kau | -5.81% | $72,205 | $160.9700 |
| 2 | vvv | -3.90% | $12,646,269 | $6.1800 |
| 3 | h | -3.22% | $13,239,849 | $0.1234 |
| 4 | stable | -3.09% | $16,040,900 | $0.0281 |
| 5 | render | -2.58% | $114,053,688 | $1.8800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $51,455,268,299 | $1.0000 |
| 2 | btc | 2.38% | $29,956,572,371 | $72,621.0000 |
| 3 | eth | 4.45% | $16,303,936,776 | $2,179.8600 |
| 4 | sol | 4.68% | $3,434,368,011 | $91.7500 |
| 5 | usdc | 0.00% | $3,377,231,530 | $0.9999 |


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
