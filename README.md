# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-25 01:27 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sn3 | 20.26% | $12,001,319 | $31.8400 |
| 2 | vvv | 16.68% | $19,192,631 | $6.6100 |
| 3 | bat | 11.33% | $64,414,489 | $0.1081 |
| 4 | tao | 11.00% | $920,905,174 | $332.3400 |
| 5 | adi | 9.70% | $1,915,038 | $3.6500 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -14.18% | $55,468,511 | $1.5600 |
| 2 | sun | -8.32% | $140,803,593 | $0.0175 |
| 3 | tibbir | -8.07% | $2,253,963 | $0.1303 |
| 4 | a7a5 | -7.16% | $7,301 | $0.0125 |
| 5 | dcr | -7.14% | $4,046,894 | $21.0500 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $68,274,179,475 | $0.9996 |
| 2 | btc | -0.20% | $41,610,135,956 | $70,680.0000 |
| 3 | eth | 0.50% | $18,367,568,669 | $2,158.4400 |
| 4 | sol | 0.14% | $4,083,003,685 | $91.0400 |
| 5 | usdc | -0.02% | $3,817,440,172 | $0.9998 |


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
