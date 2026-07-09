# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-09 02:12 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | eigen | 13.98% | $42,772,598 | $0.2474 |
| 2 | ape | 12.34% | $64,869,686 | $0.1625 |
| 3 | mana | 10.54% | $24,728,272 | $0.0748 |
| 4 | kaito | 9.03% | $137,992,390 | $0.6693 |
| 5 | hash | 8.81% | $14,123 | $0.0092 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | -71.20% | $315,511,706 | $1.3900 |
| 2 | ub | -18.58% | $10,772,612 | $0.0744 |
| 3 | gwei | -16.66% | $14,186,649 | $0.0866 |
| 4 | jto | -12.31% | $82,502,191 | $0.6347 |
| 5 | ultima | -12.19% | $11,077,362 | $2,311.2000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $43,720,190,555 | $0.9992 |
| 2 | btc | -1.40% | $26,817,070,999 | $61,996.0000 |
| 3 | usdc | -0.01% | $11,673,261,019 | $0.9998 |
| 4 | eth | -0.84% | $9,984,488,190 | $1,736.4700 |
| 5 | sol | -1.69% | $2,250,869,870 | $77.6000 |


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
