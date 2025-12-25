# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-25 01:08 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cc | 14.21% | $108,119,068 | $0.1028 |
| 2 | s | 10.11% | $45,192,828 | $0.0778 |
| 3 | cfx | 6.87% | $53,361,237 | $0.0751 |
| 4 | bat | 6.47% | $27,504,989 | $0.2193 |
| 5 | zec | 6.36% | $669,722,303 | $444.8700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -9.51% | $67,046,192 | $2.2800 |
| 2 | hnt | -6.00% | $6,057,795 | $1.5000 |
| 3 | nft | -5.55% | $20,637,960 | $0.0000 |
| 4 | h | -4.36% | $73,353,054 | $0.1546 |
| 5 | theta | -3.68% | $10,821,353 | $0.2705 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $49,633,365,894 | $0.9995 |
| 2 | btc | -0.14% | $28,175,106,327 | $87,546.0000 |
| 3 | eth | -1.09% | $14,928,420,629 | $2,939.5800 |
| 4 | usdc | 0.02% | $8,543,913,217 | $1.0000 |
| 5 | usd1 | 0.10% | $2,786,647,930 | $1.0000 |


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
