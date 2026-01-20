# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-20 01:10 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 13.67% | $57,746,903 | $30.9400 |
| 2 | night | 12.55% | $37,341,036 | $0.0623 |
| 3 | mana | 8.97% | $73,314,793 | $0.1580 |
| 4 | xtz | 7.66% | $58,221,750 | $0.6041 |
| 5 | qnt | 7.37% | $55,384,574 | $83.3700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -14.01% | $50,218,852 | $0.1695 |
| 2 | hash | -13.00% | $17,771 | $0.0247 |
| 3 | ip | -11.82% | $90,234,135 | $2.3500 |
| 4 | lit | -10.69% | $72,367,782 | $1.6200 |
| 5 | wstx | -10.21% | $1,239 | $0.3246 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $66,719,627,006 | $0.9994 |
| 2 | btc | -0.02% | $35,766,943,957 | $92,610.0000 |
| 3 | eth | -1.07% | $23,873,387,611 | $3,183.0100 |
| 4 | usdc | -0.00% | $5,002,843,155 | $0.9997 |
| 5 | sol | -0.15% | $3,622,651,713 | $133.5700 |


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
