# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-22 01:55 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | 41.40% | $391,464,552 | $1.4600 |
| 2 | m | 25.89% | $24,413,888 | $4.3500 |
| 3 | grass | 13.97% | $17,302,429 | $0.3808 |
| 4 | asteroid | 13.88% | $81,161,150 | $0.0003 |
| 5 | h | 12.94% | $36,919,712 | $0.1143 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dexe | -12.25% | $32,688,462 | $12.6500 |
| 2 | comp | -11.78% | $32,237,854 | $22.5300 |
| 3 | pieverse | -11.09% | $188,740,770 | $0.8571 |
| 4 | koge | -10.32% | $2,601,204 | $37.5300 |
| 5 | vvv | -9.22% | $15,989,402 | $8.7300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $66,441,740,631 | $1.0000 |
| 2 | btc | 0.47% | $41,916,239,454 | $76,277.0000 |
| 3 | usdc | -0.02% | $17,627,030,190 | $0.9998 |
| 4 | eth | 0.31% | $17,178,855,401 | $2,322.0400 |
| 5 | sol | 0.96% | $3,497,209,509 | $86.2700 |


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
