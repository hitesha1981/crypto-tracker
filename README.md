# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-06 01:22 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skr | 24.00% | $61,942,327 | $0.0216 |
| 2 | kau | 19.14% | $2,670,917 | $193.2800 |
| 3 | whitewhale | 11.69% | $15,048,031 | $0.1239 |
| 4 | qrl | 8.33% | $222,313 | $2.4500 |
| 5 | zk | 7.90% | $105,454,358 | $0.0242 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | b | -28.76% | $13,281,077 | $0.1350 |
| 2 | ray | -24.16% | $94,598,076 | $0.5574 |
| 3 | leo | -22.54% | $8,722,591 | $6.8800 |
| 4 | twt | -22.49% | $50,215,099 | $0.5453 |
| 5 | xmr | -22.10% | $171,065,536 | $295.5700 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.06% | $242,448,688,196 | $0.9986 |
| 2 | btc | -11.36% | $160,116,469,368 | $64,132.0000 |
| 3 | eth | -11.48% | $71,470,775,719 | $1,891.6300 |
| 4 | usdc | 0.00% | $34,361,490,181 | $0.9998 |
| 5 | xrp | -16.55% | $13,672,320,870 | $1.2400 |


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
