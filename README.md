# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-05 04:33 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cap | 32.73% | $61,770,782 | $0.0982 |
| 2 | fluid | 30.35% | $19,183,579 | $2.6900 |
| 3 | dgai | 29.51% | $54,795,564 | $0.7883 |
| 4 | beam | 23.34% | $73,072,460 | $0.0047 |
| 5 | drv | 18.27% | $20,631,458 | $0.3762 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | trump | -16.66% | $406,955,844 | $1.2500 |
| 2 | kntq | -6.18% | $5,382,666 | $0.4568 |
| 3 | rain | -5.56% | $13,268,028 | $0.0059 |
| 4 | wlfi | -3.12% | $58,643,859 | $0.0477 |
| 5 | gomining | -2.42% | $18,009,250 | $0.3849 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.05% | $59,848,528,601 | $0.9994 |
| 2 | btc | 4.92% | $36,828,208,055 | $80,404.0000 |
| 3 | eth | 7.34% | $16,240,844,219 | $2,421.5900 |
| 4 | usdc | 0.03% | $15,130,870,256 | $0.9998 |
| 5 | sol | 5.11% | $3,682,279,987 | $96.0200 |


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
