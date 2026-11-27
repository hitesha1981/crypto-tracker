# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-27 06:03 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | a7a5 | 551.44% | $1,551 | $0.0116 |
| 2 | soxlb | 14.30% | $30,171,175 | $37.5700 |
| 3 | sent | 12.62% | $10,938,451 | $0.0229 |
| 4 | sei | 11.18% | $102,097,251 | $0.0387 |
| 5 | fet | 10.92% | $72,919,328 | $0.1240 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xmr | -11.34% | $184,629,933 | $462.4300 |
| 2 | rain | -10.85% | $7,367,604 | $0.0024 |
| 3 | pearl | -6.02% | $16,095,132 | $1.8600 |
| 4 | soso | -5.78% | $4,069,988 | $0.3090 |
| 5 | dgai | -5.73% | $20,172,485 | $0.9186 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $34,948,784,352 | $0.9989 |
| 2 | btc | 1.83% | $22,562,317,918 | $61,696.0000 |
| 3 | usdc | 0.01% | $9,022,893,728 | $0.9995 |
| 4 | eth | 3.16% | $8,401,030,330 | $1,739.6000 |
| 5 | sol | 3.34% | $2,008,647,868 | $73.0300 |


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
