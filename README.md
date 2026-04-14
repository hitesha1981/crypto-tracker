# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-14 01:55 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | genius | 62.47% | $95,920,999 | $0.5367 |
| 2 | rave | 49.68% | $590,489,788 | $8.5700 |
| 3 | crclon | 16.23% | $8,125,212 | $100.2000 |
| 4 | b | 14.81% | $6,804,050 | $0.1880 |
| 5 | xpl | 14.02% | $135,673,573 | $0.1448 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -8.52% | $32,739,823 | $7.9700 |
| 2 | siren | -5.72% | $18,228,753 | $0.7818 |
| 3 | m | -5.50% | $16,376,658 | $2.7100 |
| 4 | aria | -3.53% | $61,592,743 | $0.8039 |
| 5 | tao | -3.09% | $273,140,970 | $255.6600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $84,515,990,650 | $1.0000 |
| 2 | btc | 4.55% | $55,288,774,283 | $74,418.0000 |
| 3 | eth | 7.65% | $25,067,181,829 | $2,372.5800 |
| 4 | usdc | -0.01% | $16,993,428,629 | $0.9998 |
| 5 | sol | 4.69% | $4,418,643,354 | $86.0800 |


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
