# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-17 02:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | q | 23.69% | $39,005,944 | $0.0638 |
| 2 | tia | 18.09% | $279,008,959 | $0.7034 |
| 3 | btw | 9.45% | $54,692,141 | $2.0300 |
| 4 | akt | 6.60% | $7,527,453 | $0.7311 |
| 5 | beam | 6.37% | $19,935,260 | $0.0030 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | strk | -14.27% | $159,046,105 | $0.0728 |
| 2 | cards | -11.31% | $12,966,373 | $0.2945 |
| 3 | zro | -10.34% | $127,968,973 | $1.9600 |
| 4 | pyth | -9.29% | $67,724,904 | $0.0857 |
| 5 | vvv | -8.71% | $32,448,311 | $22.9400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $51,366,942,332 | $0.9990 |
| 2 | btc | -0.76% | $27,105,400,903 | $81,450.0000 |
| 3 | usdc | 0.02% | $16,813,141,750 | $0.9998 |
| 4 | eth | -0.76% | $12,061,582,947 | $2,419.8100 |
| 5 | sol | -0.91% | $2,887,244,091 | $104.4200 |


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
