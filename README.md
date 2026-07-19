# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-19 01:58 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | b | 48.48% | $45,481,220 | $0.1707 |
| 2 | xec | 20.78% | $109,354,619 | $0.0000 |
| 3 | allo | 14.88% | $44,509,670 | $0.4526 |
| 4 | hash | 12.36% | $6,753 | $0.0088 |
| 5 | bc | 10.98% | $135,500 | $0.0171 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bonk | -10.43% | $59,981,222 | $0.0000 |
| 2 | ondo | -9.67% | $156,863,690 | $0.3431 |
| 3 | tel | -5.21% | $1,888,338 | $0.0018 |
| 4 | arb | -4.85% | $42,747,902 | $0.0879 |
| 5 | kag | -4.85% | $135,242 | $54.7400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $23,550,529,950 | $0.9993 |
| 2 | btc | 1.26% | $14,701,160,864 | $64,732.0000 |
| 3 | usdc | 0.00% | $4,487,070,270 | $0.9999 |
| 4 | eth | 0.90% | $4,438,533,493 | $1,858.0600 |
| 5 | sol | 0.60% | $918,099,926 | $75.6400 |


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
