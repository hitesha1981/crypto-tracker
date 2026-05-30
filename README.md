# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-30 02:29 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | 55.75% | $136,430,352 | $6.6500 |
| 2 | xlm | 40.38% | $2,438,695,815 | $0.2781 |
| 3 | algo | 19.38% | $129,506,528 | $0.1360 |
| 4 | hbar | 17.15% | $491,122,840 | $0.1052 |
| 5 | inj | 16.09% | $304,513,699 | $6.5000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | genius | -27.79% | $274,891,014 | $0.4503 |
| 2 | bill | -13.71% | $58,004,395 | $0.0696 |
| 3 | xpl | -5.75% | $95,445,968 | $0.0903 |
| 4 | near | -5.60% | $805,161,755 | $2.3700 |
| 5 | wal | -5.49% | $7,874,287 | $0.0586 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $56,954,790,844 | $0.9987 |
| 2 | btc | 0.26% | $34,283,955,766 | $73,522.0000 |
| 3 | eth | 0.72% | $13,634,238,968 | $2,015.0300 |
| 4 | usdc | -0.00% | $12,085,194,452 | $0.9997 |
| 5 | xlm | 40.38% | $2,438,695,815 | $0.2781 |


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
