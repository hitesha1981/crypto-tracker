# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-15 00:48 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | 72.10% | $110,104,289 | $0.0102 |
| 2 | m | 66.70% | $383,597 | $1.2900 |
| 3 | velvet | 40.50% | $73,328,282 | $1.0130 |
| 4 | cap | 15.60% | $165,409,136 | $0.0669 |
| 5 | btw | 15.30% | $43,590,214 | $0.3144 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -26.70% | $40,479,664 | $0.6474 |
| 2 | cashcat | -19.90% | $17,615,850 | $0.1306 |
| 3 | hash | -8.60% | $27,423 | $0.0070 |
| 4 | uni | -8.00% | $275,334,186 | $3.2300 |
| 5 | inj | -7.60% | $66,421,578 | $4.2800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $30,672,036,877 | $0.9991 |
| 2 | btc | -0.70% | $19,891,984,876 | $62,956.0000 |
| 3 | usdc | 0.00% | $7,869,749,020 | $0.9996 |
| 4 | eth | -0.30% | $4,918,530,071 | $1,880.8700 |
| 5 | sol | -1.10% | $1,058,736,728 | $75.3100 |


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
