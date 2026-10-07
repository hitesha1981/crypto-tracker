# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-07 03:37 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | br | 42.07% | $38,654,157 | $0.5710 |
| 2 | orca | 24.17% | $224,562,266 | $2.9300 |
| 3 | cap | 16.26% | $57,611,934 | $0.0869 |
| 4 | met | 9.95% | $42,281,857 | $0.3181 |
| 5 | pons | 8.05% | $42,797,477 | $0.4081 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | mina | -23.90% | $57,092,174 | $0.1071 |
| 2 | cashcat | -15.31% | $10,387,968 | $0.1326 |
| 3 | hash | -12.89% | $4,172 | $0.0052 |
| 4 | grass | -11.66% | $34,681,373 | $0.6510 |
| 5 | mnt | -10.20% | $35,341,433 | $0.5809 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $58,112,450,893 | $0.9999 |
| 2 | btc | -1.55% | $30,845,901,488 | $84,052.0000 |
| 3 | usdc | -0.00% | $17,200,429,192 | $0.9999 |
| 4 | eth | -3.12% | $13,918,608,457 | $2,610.2200 |
| 5 | sol | -1.35% | $2,828,018,207 | $118.2400 |


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
