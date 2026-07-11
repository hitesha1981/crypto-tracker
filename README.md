# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-11 01:57 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cashcat | 51.28% | $43,119,680 | $0.1622 |
| 2 | b | 41.06% | $31,527,598 | $0.2266 |
| 3 | virtual | 16.83% | $153,171,762 | $0.6266 |
| 4 | beat | 16.16% | $18,974,925 | $2.6100 |
| 5 | tibbir | 12.68% | $1,620,278 | $0.1348 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | -25.23% | $130,556,457 | $0.8691 |
| 2 | gwei | -19.57% | $8,919,930 | $0.0636 |
| 3 | awe | -11.99% | $6,348,672 | $0.0576 |
| 4 | edge | -9.99% | $14,447,235 | $0.4067 |
| 5 | nex | -8.09% | $7,843,242 | $0.0000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $41,676,343,752 | $0.9993 |
| 2 | btc | 0.56% | $26,475,678,089 | $64,038.0000 |
| 3 | usdc | 0.01% | $11,272,200,129 | $0.9999 |
| 4 | eth | 1.36% | $7,966,814,638 | $1,790.4300 |
| 5 | sol | -1.85% | $1,877,395,745 | $77.6000 |


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
