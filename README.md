# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-25 01:27 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skr | 32.08% | $169,831,548 | $0.0248 |
| 2 | power | 29.53% | $57,692,987 | $0.6906 |
| 3 | dexe | 17.42% | $25,111,139 | $3.4300 |
| 4 | siren | 16.59% | $23,216,771 | $0.3361 |
| 5 | aero | 16.06% | $27,226,803 | $0.3425 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | mwc | -11.75% | $134,965 | $11.1200 |
| 2 | b | -7.81% | $3,451,705 | $0.1276 |
| 3 | hash | -7.40% | $5,300 | $0.0161 |
| 4 | inj | -3.96% | $67,943,556 | $3.2500 |
| 5 | river | -3.29% | $20,860,931 | $8.8600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $70,376,954,397 | $1.0000 |
| 2 | btc | 2.64% | $45,786,849,300 | $66,121.0000 |
| 3 | eth | 3.68% | $19,683,340,415 | $1,917.7200 |
| 4 | usdc | 0.01% | $4,187,389,816 | $1.0000 |
| 5 | sol | 5.74% | $3,494,042,123 | $82.1400 |


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
