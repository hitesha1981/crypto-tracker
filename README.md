# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-09 01:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | 32.21% | $41,802,287 | $0.3760 |
| 2 | jasmy | 11.27% | $139,196,277 | $0.0095 |
| 3 | pol | 6.98% | $144,855,119 | $0.1387 |
| 4 | stable | 6.14% | $25,640,666 | $0.0149 |
| 5 | xtz | 4.36% | $32,751,794 | $0.5954 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zec | -9.38% | $1,494,586,931 | $434.7600 |
| 2 | river | -8.82% | $27,507,559 | $15.0700 |
| 3 | pump | -8.26% | $131,352,377 | $0.0022 |
| 4 | xpl | -7.29% | $127,916,236 | $0.1657 |
| 5 | pepe | -6.67% | $776,334,817 | $0.0000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $80,616,480,538 | $0.9991 |
| 2 | btc | -0.06% | $47,765,485,656 | $91,223.0000 |
| 3 | eth | -1.77% | $24,282,481,704 | $3,113.5700 |
| 4 | usdc | 0.01% | $13,710,790,893 | $0.9999 |
| 5 | sol | 1.70% | $5,389,763,121 | $139.0200 |


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
