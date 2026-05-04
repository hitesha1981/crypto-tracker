# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-04 02:08 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | 75.29% | $452,112,927 | $2.4800 |
| 2 | tag | 48.71% | $40,325,345 | $0.0017 |
| 3 | skyai | 31.08% | $156,928,020 | $0.5823 |
| 4 | bsb | 28.69% | $31,334,848 | $0.8446 |
| 5 | b | 25.66% | $156,552,853 | $0.4157 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | -19.98% | $78,714,266 | $0.1238 |
| 2 | lunc | -9.83% | $130,080,989 | $0.0001 |
| 3 | gno | -7.27% | $9,749,860 | $128.0600 |
| 4 | ape | -5.00% | $47,829,522 | $0.1678 |
| 5 | mega | -4.99% | $245,531,101 | $0.1216 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $42,472,999,875 | $0.9997 |
| 2 | btc | 1.93% | $25,724,278,781 | $79,773.0000 |
| 3 | eth | 2.11% | $11,642,849,412 | $2,353.8800 |
| 4 | usdc | -0.01% | $7,339,964,753 | $0.9997 |
| 5 | sol | 1.42% | $2,162,928,418 | $84.9500 |


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
