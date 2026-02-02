# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-02 01:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zk | 32.67% | $616,504,430 | $0.0310 |
| 2 | ultima | 20.18% | $11,089,758 | $5,765.3600 |
| 3 | stable | 17.47% | $41,881,309 | $0.0265 |
| 4 | myx | 13.00% | $26,016,588 | $5.4700 |
| 5 | dcr | 9.22% | $7,769,029 | $19.6400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -30.47% | $114,255,164 | $18.0900 |
| 2 | kag | -9.29% | $2,820,498 | $83.5900 |
| 3 | twt | -8.99% | $18,847,636 | $0.6695 |
| 4 | xmr | -8.61% | $134,355,660 | $418.2100 |
| 5 | liquideth | -7.07% | $103 | $2,436.2700 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $107,072,291,075 | $0.9991 |
| 2 | btc | -1.27% | $59,180,262,441 | $77,520.0000 |
| 3 | eth | -5.67% | $42,607,550,875 | $2,299.1800 |
| 4 | usdc | 0.01% | $6,530,546,789 | $0.9997 |
| 5 | sol | -2.82% | $6,367,063,927 | $101.6400 |


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
