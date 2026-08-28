# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-28 08:20 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | trump | 23.19% | $1,209,571,544 | $2.8300 |
| 2 | tibbir | 14.27% | $3,091,342 | $0.2891 |
| 3 | ena | 11.42% | $2,360,672,383 | $0.1694 |
| 4 | safe | 10.28% | $2,897,506 | $0.1754 |
| 5 | melania | 10.14% | $26,878,818 | $0.1223 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rune | -18.17% | $27,503,779 | $0.5076 |
| 2 | ff | -12.89% | $14,017,487 | $0.0887 |
| 3 | jto | -9.61% | $62,707,211 | $0.4808 |
| 4 | cashcat | -9.30% | $38,265,532 | $0.2105 |
| 5 | s | -7.36% | $20,558,195 | $0.0296 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $67,948,899,616 | $1.0000 |
| 2 | btc | 0.39% | $36,589,626,045 | $79,812.0000 |
| 3 | usdc | 0.01% | $20,303,221,084 | $1.0000 |
| 4 | eth | -0.63% | $15,532,918,364 | $2,500.8300 |
| 5 | sol | 3.51% | $6,586,045,129 | $106.5800 |


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
