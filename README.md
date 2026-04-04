# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-04 01:28 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | edge | 38.88% | $282,575,617 | $1.0640 |
| 2 | gas | 21.92% | $96,308,764 | $1.9200 |
| 3 | trac | 12.07% | $14,445,479 | $0.3038 |
| 4 | kite | 9.49% | $113,705,494 | $0.1372 |
| 5 | algo | 9.03% | $202,573,798 | $0.1216 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -16.45% | $17,725,239 | $0.1546 |
| 2 | zk | -10.47% | $21,738,624 | $0.0151 |
| 3 | ray | -8.89% | $36,823,714 | $0.6230 |
| 4 | river | -7.52% | $33,263,374 | $11.7200 |
| 5 | sent | -7.02% | $17,126,236 | $0.0161 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $39,109,173,356 | $0.9999 |
| 2 | btc | -0.01% | $24,468,437,378 | $66,850.0000 |
| 3 | eth | -0.41% | $10,097,400,312 | $2,050.2100 |
| 4 | usdc | 0.00% | $6,213,663,686 | $1.0000 |
| 5 | sol | 0.89% | $2,319,078,214 | $80.0900 |


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
