# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-02 01:10 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 34.71% | $63,806,694 | $15.2800 |
| 2 | pepe | 20.89% | $591,165,074 | $0.0000 |
| 3 | aero | 16.30% | $43,857,682 | $0.4706 |
| 4 | lit | 14.25% | $19,283,183 | $2.6600 |
| 5 | ip | 13.78% | $189,479,840 | $1.9400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hash | -10.76% | $2,270 | $0.0267 |
| 2 | khype | -5.78% | $6,100,695 | $24.6300 |
| 3 | hype | -5.75% | $226,000,713 | $24.4100 |
| 4 | whype | -5.63% | $63,986,870 | $24.4500 |
| 5 | jst | -5.49% | $29,265,595 | $0.0393 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $39,480,175,497 | $0.9989 |
| 2 | btc | 1.06% | $21,883,604,777 | $88,646.0000 |
| 3 | eth | 0.82% | $10,489,251,516 | $3,001.0300 |
| 4 | usdc | 0.01% | $5,532,708,803 | $0.9999 |
| 5 | sol | 1.05% | $2,686,737,865 | $126.5700 |


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
