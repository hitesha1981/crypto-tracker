# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-14 02:32 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | 22.87% | $73,026,097 | $5.9300 |
| 2 | ub | 20.35% | $59,069,421 | $0.2065 |
| 3 | river | 13.36% | $15,730,425 | $7.0400 |
| 4 | ff | 12.40% | $83,629,164 | $0.0871 |
| 5 | kite | 11.49% | $98,023,858 | $0.2142 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lunc | -15.04% | $75,567,242 | $0.0001 |
| 2 | skyai | -13.62% | $44,646,460 | $0.4702 |
| 3 | vvv | -13.11% | $83,219,048 | $13.3800 |
| 4 | ath | -10.07% | $43,208,635 | $0.0065 |
| 5 | ton | -9.95% | $387,863,404 | $2.0800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $71,485,992,260 | $0.9996 |
| 2 | btc | -1.77% | $45,012,582,002 | $79,609.0000 |
| 3 | eth | -1.40% | $13,742,950,021 | $2,262.0900 |
| 4 | usdc | -0.00% | $12,719,777,504 | $0.9998 |
| 5 | sol | -4.41% | $3,886,302,057 | $91.1000 |


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
