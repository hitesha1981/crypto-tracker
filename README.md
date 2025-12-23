# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-23 01:08 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | 43.00% | $208,714,668 | $0.2075 |
| 2 | crv | 7.78% | $104,434,512 | $0.3796 |
| 3 | night | 6.08% | $4,124,029,258 | $0.1001 |
| 4 | myx | 5.23% | $43,442,541 | $3.3700 |
| 5 | jasmy | 4.63% | $37,992,181 | $0.0064 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | -16.66% | $57,990,067 | $0.3511 |
| 2 | m | -9.22% | $11,183,464 | $1.3500 |
| 3 | cc | -8.35% | $39,207,464 | $0.0871 |
| 4 | aave | -7.65% | $693,458,755 | $149.4500 |
| 5 | rain | -6.54% | $36,613,144 | $0.0072 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $68,985,266,254 | $0.9995 |
| 2 | btc | 0.05% | $40,639,202,151 | $88,772.0000 |
| 3 | eth | 0.03% | $21,148,505,394 | $3,027.9000 |
| 4 | usdc | -0.01% | $11,927,987,816 | $0.9999 |
| 5 | night | 6.08% | $4,124,029,258 | $0.1001 |


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
