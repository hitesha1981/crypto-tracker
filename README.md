# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-17 01:59 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kaito | 11.31% | $49,615,748 | $0.8423 |
| 2 | trac | 11.09% | $6,457,643 | $0.2987 |
| 3 | ub | 8.41% | $11,292,689 | $0.0814 |
| 4 | tibbir | 7.79% | $1,034,987 | $0.1151 |
| 5 | cro | 7.39% | $36,486,431 | $0.0597 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | fartcoin | -11.14% | $14,723,524 | $0.1330 |
| 2 | lit | -10.43% | $50,479,146 | $2.1800 |
| 3 | hype | -10.38% | $525,036,167 | $59.7300 |
| 4 | jto | -9.49% | $32,411,899 | $0.5575 |
| 5 | bp | -9.33% | $2,065,633 | $0.4853 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $43,255,515,312 | $0.9992 |
| 2 | btc | -1.82% | $27,330,261,643 | $63,506.0000 |
| 3 | usdc | 0.02% | $10,829,297,760 | $1.0000 |
| 4 | eth | -3.77% | $10,365,868,120 | $1,849.4500 |
| 5 | sol | -2.64% | $1,686,168,101 | $75.0000 |


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
