# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-19 05:21 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pearl | 27.44% | $59,753,944 | $2.3400 |
| 2 | pieverse | 26.46% | $172,404,115 | $2.7400 |
| 3 | btw | 23.73% | $7,098,573 | $0.5520 |
| 4 | lunc | 19.31% | $21,645,119 | $0.0000 |
| 5 | sent | 15.08% | $43,640,834 | $0.0223 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hash | -13.26% | $6,774 | $0.0065 |
| 2 | cap | -10.87% | $8,039,797 | $0.0899 |
| 3 | beam | -10.18% | $6,200,538 | $0.0036 |
| 4 | cards | -8.24% | $5,029,936 | $0.1561 |
| 5 | mon | -7.56% | $16,674,909 | $0.0137 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $47,740,657,035 | $0.9992 |
| 2 | btc | -1.94% | $31,904,443,540 | $63,356.0000 |
| 3 | usdc | 0.01% | $13,873,975,255 | $0.9996 |
| 4 | eth | -0.82% | $10,698,110,468 | $1,794.8900 |
| 5 | sol | -0.94% | $2,151,100,004 | $74.4200 |


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
