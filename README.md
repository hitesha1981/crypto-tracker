# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-11 03:59 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 18.89% | $12,217,795 | $1.1900 |
| 2 | lit | 11.46% | $97,012,202 | $3.5200 |
| 3 | icp | 8.36% | $49,764,147 | $2.5900 |
| 4 | anvl | 7.79% | $522,700 | $0.0021 |
| 5 | zro | 7.47% | $60,593,117 | $1.5800 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pieverse | -12.53% | $39,683,722 | $1.7400 |
| 2 | cards | -10.67% | $14,220,460 | $0.2140 |
| 3 | zec | -10.53% | $1,262,746,912 | $1,029.0200 |
| 4 | vvv | -10.14% | $57,421,981 | $19.2700 |
| 5 | rain | -9.38% | $14,955,514 | $0.0041 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $53,068,639,153 | $0.9991 |
| 2 | btc | -1.05% | $31,681,863,326 | $73,692.0000 |
| 3 | usdc | 0.01% | $14,454,637,173 | $0.9995 |
| 4 | eth | -2.45% | $14,016,434,055 | $2,060.2500 |
| 5 | sol | -2.82% | $3,038,943,307 | $83.2800 |


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
