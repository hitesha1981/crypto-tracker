# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-10 01:20 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dexe | 15.09% | $23,832,284 | $4.7000 |
| 2 | grass | 14.57% | $20,595,401 | $0.3385 |
| 3 | pippin | 14.36% | $24,729,252 | $0.3812 |
| 4 | hype | 12.10% | $503,627,161 | $34.2700 |
| 5 | zec | 9.10% | $294,241,301 | $216.4400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -13.98% | $24,850,459 | $11.9700 |
| 2 | om | -11.03% | $135,773 | $0.0305 |
| 3 | qrl | -5.70% | $48,399 | $1.4100 |
| 4 | rlb | -5.21% | $658,221 | $0.0706 |
| 5 | wif | -3.33% | $94,170,223 | $0.1727 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $81,440,109,823 | $1.0000 |
| 2 | btc | 3.92% | $51,831,990,092 | $68,987.0000 |
| 3 | eth | 3.33% | $24,900,250,760 | $2,014.8100 |
| 4 | usdc | -0.00% | $12,582,121,791 | $1.0000 |
| 5 | sol | 4.02% | $4,389,156,523 | $85.6400 |


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
