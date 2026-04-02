# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-02 01:44 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sto | 148.42% | $499,920,608 | $0.5060 |
| 2 | ont | 50.87% | $310,579,815 | $0.1189 |
| 3 | xpl | 13.50% | $103,317,044 | $0.1034 |
| 4 | vsn | 11.57% | $10,150,912 | $0.0585 |
| 5 | twt | 9.68% | $36,388,070 | $0.3934 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -43.31% | $99,153,783 | $0.2395 |
| 2 | qubic | -11.89% | $3,843,318 | $0.0000 |
| 3 | hash | -8.45% | $17,940 | $0.0104 |
| 4 | crclon | -7.79% | $7,391,333 | $89.0400 |
| 5 | ray | -7.65% | $131,075,035 | $0.6374 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.07% | $79,130,117,527 | $0.9998 |
| 2 | btc | -0.99% | $49,732,360,814 | $67,159.0000 |
| 3 | eth | 0.10% | $21,087,850,819 | $2,094.7100 |
| 4 | usdc | -0.01% | $14,305,584,582 | $0.9996 |
| 5 | sol | -4.22% | $5,071,227,686 | $79.4300 |


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
