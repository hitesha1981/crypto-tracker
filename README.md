# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-23 02:42 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | prl | 49.54% | $6,337,771 | $1.4800 |
| 2 | marscoin | 38.32% | $119,458,978 | $0.1411 |
| 3 | bch | 27.44% | $1,389,424,945 | $340.0900 |
| 4 | useless | 23.30% | $113,660,237 | $0.3376 |
| 5 | bsv | 21.40% | $54,999,026 | $23.2600 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | 龙虾 | -36.46% | $24,340,647 | $0.1421 |
| 2 | stonk | -16.37% | $51,855,734 | $0.3124 |
| 3 | ake | -14.24% | $36,630,809 | $0.0471 |
| 4 | m | -9.64% | $940,788 | $1.3000 |
| 5 | rail | -6.19% | $836,858 | $3.0100 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $77,170,245,196 | $0.9998 |
| 2 | btc | 0.91% | $42,062,015,780 | $86,522.0000 |
| 3 | usdc | 0.01% | $20,382,228,153 | $0.9999 |
| 4 | eth | 0.43% | $15,839,593,876 | $2,757.5200 |
| 5 | xrp | 4.48% | $6,391,187,228 | $1.5900 |


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
