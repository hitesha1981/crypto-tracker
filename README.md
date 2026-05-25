# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-25 02:45 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rail | 25.57% | $7,405,446 | $4.2100 |
| 2 | bill | 16.58% | $95,527,440 | $0.1099 |
| 3 | ub | 12.29% | $29,008,642 | $0.1546 |
| 4 | dexe | 10.56% | $27,322,408 | $15.1100 |
| 5 | h | 10.50% | $45,534,159 | $0.2319 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bsb | -25.02% | $76,718,564 | $0.9352 |
| 2 | beat | -18.14% | $47,772,195 | $1.1900 |
| 3 | fluid | -6.27% | $2,584,531 | $1.6100 |
| 4 | cheems | -5.65% | $1,430,350 | $0.0000 |
| 5 | syrup | -5.52% | $5,763,216 | $0.1902 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $40,010,107,570 | $0.9988 |
| 2 | btc | 0.43% | $23,723,272,699 | $77,050.0000 |
| 3 | eth | -1.14% | $10,010,493,817 | $2,096.1100 |
| 4 | usdc | 0.00% | $8,620,275,536 | $0.9998 |
| 5 | sol | -0.81% | $2,421,122,090 | $85.0200 |


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
