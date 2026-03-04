# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-04 01:21 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 23.55% | $41,778,706 | $18.4700 |
| 2 | form | 19.16% | $59,381,312 | $0.3265 |
| 3 | kite | 10.82% | $230,714,529 | $0.2354 |
| 4 | xpl | 9.99% | $159,264,949 | $0.1148 |
| 5 | xdc | 8.63% | $23,202,128 | $0.0358 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | -32.77% | $56,587,216 | $0.3775 |
| 2 | vvv | -18.40% | $45,113,044 | $5.9000 |
| 3 | aave | -9.26% | $496,868,091 | $110.3600 |
| 4 | siren | -8.91% | $18,108,288 | $0.3981 |
| 5 | bera | -6.81% | $24,078,178 | $0.5558 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $84,131,210,961 | $1.0000 |
| 2 | btc | -1.23% | $53,085,842,728 | $68,075.0000 |
| 3 | eth | -2.95% | $24,108,068,253 | $1,974.7700 |
| 4 | usdc | 0.00% | $14,068,428,229 | $0.9999 |
| 5 | sol | 0.09% | $5,279,031,595 | $86.8600 |


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
