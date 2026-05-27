# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-27 02:44 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rain | 43.55% | $43,038,654 | $0.0116 |
| 2 | trac | 11.64% | $14,520,142 | $0.4432 |
| 3 | ub | 11.19% | $30,584,329 | $0.2142 |
| 4 | ath | 9.38% | $22,106,676 | $0.0066 |
| 5 | wld | 8.85% | $577,038,596 | $0.3591 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skyai | -20.83% | $28,065,602 | $0.2144 |
| 2 | grass | -14.03% | $57,264,126 | $0.5002 |
| 3 | zec | -10.08% | $929,590,224 | $564.3100 |
| 4 | crclon | -9.17% | $15,281,699 | $103.1400 |
| 5 | near | -8.94% | $1,223,933,302 | $2.4800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.04% | $65,169,866,886 | $0.9986 |
| 2 | btc | -1.19% | $38,861,156,230 | $75,625.0000 |
| 3 | usdc | 0.01% | $17,266,800,361 | $0.9998 |
| 4 | eth | -0.91% | $14,331,707,008 | $2,067.2300 |
| 5 | sol | -0.47% | $2,711,107,549 | $83.5700 |


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
