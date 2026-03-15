# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-15 01:46 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | grx | 19.07% | $25,532,445 | $11.8100 |
| 2 | dexe | 13.22% | $20,644,626 | $5.3300 |
| 3 | xcn | 10.76% | $18,520,425 | $0.0055 |
| 4 | mnt | 10.56% | $97,461,477 | $0.7876 |
| 5 | tao | 10.21% | $245,677,244 | $261.0000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btse | -12.41% | $13,059,522 | $1.4800 |
| 2 | qrl | -7.81% | $50,124 | $1.4100 |
| 3 | pi | -7.65% | $74,103,975 | $0.1988 |
| 4 | sky | -7.53% | $12,654,870 | $0.0726 |
| 5 | hash | -6.31% | $4,017 | $0.0125 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $36,942,406,975 | $1.0000 |
| 2 | btc | 0.08% | $22,279,936,372 | $70,937.0000 |
| 3 | eth | -0.30% | $8,907,440,898 | $2,086.8400 |
| 4 | usdc | 0.00% | $2,687,828,441 | $0.9999 |
| 5 | sol | -0.60% | $1,860,861,293 | $87.6700 |


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
