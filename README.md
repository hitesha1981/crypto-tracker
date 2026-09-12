# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-12 02:28 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | prl | 25.55% | $1,992,416 | $0.5894 |
| 2 | ai | 24.35% | $38,966,862 | $0.2606 |
| 3 | mina | 18.46% | $31,424,312 | $0.1085 |
| 4 | stonk | 11.44% | $136,995,934 | $0.2936 |
| 5 | ray | 10.60% | $332,690,360 | $1.7100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | -9.71% | $40,924,846 | $0.0139 |
| 2 | ff | -9.57% | $16,433,771 | $0.1521 |
| 3 | atom | -8.87% | $52,614,966 | $1.6400 |
| 4 | apt | -6.24% | $95,211,601 | $0.6138 |
| 5 | trac | -5.79% | $7,405,918 | $0.3337 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $70,008,476,337 | $0.9999 |
| 2 | btc | 0.69% | $34,115,134,046 | $77,300.0000 |
| 3 | eth | 2.78% | $24,603,355,657 | $2,513.8400 |
| 4 | usdc | -0.01% | $19,255,854,980 | $0.9999 |
| 5 | sol | 2.72% | $4,555,883,337 | $101.8200 |


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
