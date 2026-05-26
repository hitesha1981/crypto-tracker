# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-26 02:33 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | 21.73% | $29,860,483 | $0.1894 |
| 2 | dexe | 15.17% | $47,869,895 | $17.4200 |
| 3 | near | 13.54% | $1,090,819,597 | $2.7000 |
| 4 | grass | 13.23% | $51,444,838 | $0.5850 |
| 5 | wld | 12.38% | $238,135,433 | $0.3285 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bsb | -27.25% | $100,060,681 | $0.6788 |
| 2 | nex | -22.06% | $171,943,838 | $0.0000 |
| 3 | bill | -21.31% | $117,750,420 | $0.0880 |
| 4 | beat | -17.85% | $21,163,336 | $0.9962 |
| 5 | skyai | -17.75% | $28,714,322 | $0.2700 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $41,460,343,230 | $0.9990 |
| 2 | btc | -0.60% | $22,174,345,036 | $76,601.0000 |
| 3 | usdc | -0.01% | $10,180,396,248 | $0.9997 |
| 4 | eth | -0.52% | $9,940,776,444 | $2,087.4100 |
| 5 | sol | -1.32% | $2,002,195,183 | $83.9300 |


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
