# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-04 01:22 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | wstx | 19.71% | $703 | $0.3090 |
| 2 | dcr | 6.18% | $4,908,890 | $20.1600 |
| 3 | wlfi | 5.46% | $135,962,061 | $0.1361 |
| 4 | jup | 5.11% | $85,780,026 | $0.1984 |
| 5 | atom | 4.87% | $57,445,087 | $2.0600 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -26.48% | $65,989,129 | $12.5100 |
| 2 | tel | -8.76% | $4,389,076 | $0.0029 |
| 3 | stable | -8.42% | $54,268,381 | $0.0274 |
| 4 | lit | -6.22% | $57,203,702 | $1.5100 |
| 5 | aero | -5.49% | $26,966,337 | $0.3810 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.04% | $131,751,331,399 | $0.9987 |
| 2 | btc | -2.93% | $76,370,347,792 | $76,394.0000 |
| 3 | eth | -3.27% | $49,855,336,135 | $2,267.7000 |
| 4 | usdc | -0.01% | $12,113,038,121 | $0.9997 |
| 5 | sol | -4.58% | $6,337,565,154 | $98.9400 |


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
