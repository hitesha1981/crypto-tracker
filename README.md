# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-29 02:46 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cx | 36.52% | $1,696,760 | $0.0782 |
| 2 | velvet | 27.48% | $64,661,813 | $2.0200 |
| 3 | gwei | 19.08% | $16,153,752 | $0.1554 |
| 4 | slx | 13.46% | $53,456,351 | $0.5807 |
| 5 | wif | 6.52% | $55,634,217 | $0.1762 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skyai | -44.16% | $69,959,658 | $0.1385 |
| 2 | pieverse | -16.16% | $15,336,786 | $0.7036 |
| 3 | lab | -15.72% | $28,194,995 | $14.4600 |
| 4 | m | -11.57% | $13,346,824 | $0.6395 |
| 5 | btw | -10.03% | $16,852,973 | $0.0543 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $30,217,104,851 | $0.9983 |
| 2 | btc | -0.65% | $18,804,364,169 | $59,658.0000 |
| 3 | usdc | -0.02% | $7,526,555,123 | $0.9996 |
| 4 | eth | 0.27% | $6,807,514,391 | $1,573.4400 |
| 5 | sol | 1.79% | $2,047,736,448 | $71.9000 |


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
