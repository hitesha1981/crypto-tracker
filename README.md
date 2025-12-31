# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-31 01:10 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cc | 17.60% | $41,667,054 | $0.1481 |
| 2 | uds | 12.25% | $1,213,742 | $2.7700 |
| 3 | xpl | 7.75% | $88,022,346 | $0.1663 |
| 4 | chz | 7.60% | $70,944,247 | $0.0397 |
| 5 | h | 7.21% | $77,496,240 | $0.1826 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -13.96% | $40,968,537 | $1.9300 |
| 2 | hash | -7.42% | $17,824 | $0.0291 |
| 3 | mnt | -4.31% | $50,312,857 | $0.9667 |
| 4 | wif | -4.07% | $111,506,559 | $0.2772 |
| 5 | morpho | -4.00% | $7,696,225 | $1.1200 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $64,297,399,108 | $0.9989 |
| 2 | btc | 1.19% | $39,964,242,637 | $88,143.0000 |
| 3 | eth | 0.94% | $19,228,376,873 | $2,959.6500 |
| 4 | usdc | 0.01% | $10,933,398,231 | $0.9998 |
| 5 | sol | 1.66% | $3,463,853,828 | $124.8500 |


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
