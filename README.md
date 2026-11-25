# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-25 06:22 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 17.02% | $4,499,211 | $0.8300 |
| 2 | sky | 3.82% | $23,720,902 | $0.0414 |
| 3 | xmr | 2.82% | $123,234,196 | $509.0500 |
| 4 | lunc | 1.84% | $17,400,374 | $0.0000 |
| 5 | stable | 1.73% | $7,520,849 | $0.0238 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | mon | -26.57% | $119,487,263 | $0.0100 |
| 2 | hash | -17.94% | $886 | $0.0061 |
| 3 | bp | -14.20% | $3,927,940 | $0.7742 |
| 4 | zro | -12.53% | $84,158,858 | $0.9974 |
| 5 | bc | -10.34% | $194,308 | $0.0339 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $43,878,222,272 | $0.9989 |
| 2 | btc | -2.16% | $28,213,222,683 | $59,174.0000 |
| 3 | usdc | -0.01% | $12,816,745,206 | $0.9995 |
| 4 | eth | -2.52% | $9,761,778,630 | $1,657.8700 |
| 5 | sol | -4.23% | $2,550,504,675 | $68.6000 |


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
