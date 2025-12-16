# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-16 12:14 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | 28.89% | $78,847,803 | $0.4891 |
| 2 | hash | 17.05% | $78,816 | $0.0310 |
| 3 | xdc | 4.41% | $44,212,447 | $0.0491 |
| 4 | apepe | 3.96% | $17,300,228 | $0.0000 |
| 5 | cc | 2.99% | $13,526,459 | $0.0732 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -21.53% | $84,001,761 | $2.1900 |
| 2 | merl | -16.05% | $34,901,885 | $0.3997 |
| 3 | night | -10.83% | $1,261,570,577 | $0.0552 |
| 4 | ultima | -9.72% | $14,669,297 | $5,499.7700 |
| 5 | tel | -9.38% | $5,947,859 | $0.0041 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $88,464,659,907 | $1.0000 |
| 2 | btc | -2.43% | $53,831,715,009 | $87,273.0000 |
| 3 | eth | -6.00% | $31,258,052,243 | $2,961.4100 |
| 4 | usdc | 0.03% | $13,383,882,405 | $1.0000 |
| 5 | sol | -2.44% | $5,923,003,582 | $128.7100 |


<!-- END_DYNAMIC_CONTENT -->

## How to generate the coingecko demo public api key
[coingecko-api-key-docs]: https://support.coingecko.com/hc/en-us/articles/21880397454233-User-Guide-How-to-sign-up-for-CoinGecko-Demo-API-and-generate-an-API-key

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
