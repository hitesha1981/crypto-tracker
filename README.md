# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-01 02:55 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pons | 45.13% | $104,689,294 | $0.4059 |
| 2 | arb | 33.08% | $345,034,921 | $0.1122 |
| 3 | safe | 29.83% | $6,295,030 | $0.2235 |
| 4 | crv | 18.24% | $90,366,561 | $0.3523 |
| 5 | cashcat | 18.10% | $48,821,475 | $0.2210 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hnt | -13.48% | $75,313,930 | $0.6127 |
| 2 | ff | -8.69% | $6,071,245 | $0.0847 |
| 3 | drv | -8.40% | $4,895,218 | $0.1393 |
| 4 | apepe | -4.76% | $10,330,386 | $0.0000 |
| 5 | skr | -4.76% | $279,273,523 | $0.0308 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $50,632,532,274 | $0.9997 |
| 2 | btc | 1.24% | $29,392,968,248 | $78,393.0000 |
| 3 | usdc | 0.01% | $15,754,736,953 | $0.9999 |
| 4 | eth | 2.46% | $11,434,079,183 | $2,461.7400 |
| 5 | sol | 1.91% | $3,105,816,444 | $103.3200 |


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
