# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-19 01:27 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | awe | 22.75% | $31,235,642 | $0.1038 |
| 2 | hnt | 17.38% | $22,675,330 | $1.6700 |
| 3 | wlfi | 12.17% | $478,672,990 | $0.1191 |
| 4 | ban | 9.16% | $7,726,380 | $0.1184 |
| 5 | sky | 8.77% | $18,154,130 | $0.0670 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | myx | -30.92% | $32,357,361 | $1.0030 |
| 2 | river | -15.18% | $27,282,562 | $7.8600 |
| 3 | tibbir | -13.51% | $6,534,389 | $0.1303 |
| 4 | op | -12.04% | $85,000,581 | $0.1635 |
| 5 | hash | -11.01% | $13,281 | $0.0181 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $60,573,159,011 | $0.9996 |
| 2 | btc | -0.66% | $34,995,663,316 | $66,693.0000 |
| 3 | eth | -0.68% | $19,440,290,322 | $1,963.3500 |
| 4 | usdc | -0.01% | $9,931,743,888 | $0.9999 |
| 5 | sol | -3.24% | $3,358,454,161 | $81.6700 |


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
