# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-18 01:28 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hash | 18.20% | $101,564 | $0.0204 |
| 2 | jto | 16.58% | $195,895,098 | $0.3147 |
| 3 | tibbir | 15.52% | $7,755,475 | $0.1507 |
| 4 | morpho | 10.92% | $26,532,033 | $1.5100 |
| 5 | pi | 7.08% | $29,707,693 | $0.1857 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -27.93% | $22,325,279 | $9.2500 |
| 2 | pippin | -23.20% | $73,099,148 | $0.4948 |
| 3 | myx | -22.70% | $37,078,681 | $1.4500 |
| 4 | awe | -13.17% | $6,621,733 | $0.0848 |
| 5 | mwc | -12.76% | $139,959 | $15.2600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $64,349,616,415 | $0.9996 |
| 2 | btc | -2.51% | $37,687,112,218 | $67,106.0000 |
| 3 | eth | -1.28% | $20,109,173,046 | $1,976.9700 |
| 4 | usdc | 0.01% | $4,005,453,208 | $1.0000 |
| 5 | sol | -2.90% | $3,336,924,095 | $84.3200 |


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
