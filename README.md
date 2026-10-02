# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-02 03:27 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rail | 31.09% | $1,519,741 | $3.1200 |
| 2 | super | 18.09% | $39,165,831 | $0.2372 |
| 3 | ai | 17.38% | $30,320,961 | $0.1775 |
| 4 | jasmy | 11.23% | $73,024,440 | $0.0057 |
| 5 | btw | 8.36% | $37,190,149 | $1.4400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | shfl | -21.68% | $1,165,789 | $0.4512 |
| 2 | bp | -17.24% | $24,081,004 | $1.2900 |
| 3 | qnt | -16.07% | $456,025,732 | $250.2500 |
| 4 | ena | -9.47% | $528,569,593 | $0.2412 |
| 5 | hash | -7.79% | $10,308 | $0.0060 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $66,328,888,043 | $0.9997 |
| 2 | btc | 2.14% | $34,555,843,635 | $85,184.0000 |
| 3 | usdc | 0.01% | $21,609,301,091 | $0.9999 |
| 4 | eth | 1.10% | $14,137,824,483 | $2,714.2200 |
| 5 | sol | 1.70% | $3,508,035,385 | $119.9500 |


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
