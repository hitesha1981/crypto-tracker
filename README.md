# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-18 02:33 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | mcat | 255.35% | $15,763,479 | $0.8520 |
| 2 | geod | 50.65% | $31,806,808 | $0.3394 |
| 3 | prl | 25.78% | $2,535,210 | $0.7797 |
| 4 | near | 25.73% | $1,494,538,813 | $3.2800 |
| 5 | ai | 23.69% | $45,909,475 | $0.3355 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | trac | -5.84% | $16,776,193 | $0.3301 |
| 2 | zcat | -5.02% | $8,668,486 | $0.1298 |
| 3 | btw | -4.53% | $8,245,253 | $0.7053 |
| 4 | ff | -4.10% | $13,826,242 | $0.1314 |
| 5 | antfun | -4.01% | $11,415,235 | $0.0865 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $49,665,892,442 | $0.9992 |
| 2 | btc | 0.96% | $23,244,362,876 | $76,880.0000 |
| 3 | usdc | -0.01% | $15,157,966,927 | $0.9996 |
| 4 | eth | 1.61% | $11,886,966,957 | $2,460.0000 |
| 5 | sol | 3.57% | $3,217,758,378 | $102.5600 |


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
