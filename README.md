# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-04 02:10 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ansem | 91.12% | $77,991,043 | $0.3211 |
| 2 | magma | 51.16% | $24,018,133 | $0.7838 |
| 3 | nex | 48.19% | $34,725,441 | $0.0000 |
| 4 | pepe | 12.78% | $219,055,008 | $0.0000 |
| 5 | kite | 12.44% | $41,106,272 | $0.1186 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | -48.02% | $52,581,140 | $5.8900 |
| 2 | cx | -16.08% | $540,200 | $0.0767 |
| 3 | beat | -15.43% | $18,221,689 | $2.6900 |
| 4 | tac | -14.29% | $6,026,731 | $0.0302 |
| 5 | vvv | -11.43% | $28,639,219 | $12.2300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.04% | $44,034,561,965 | $0.9991 |
| 2 | btc | 1.66% | $26,081,487,175 | $62,473.0000 |
| 3 | eth | 2.38% | $9,391,320,239 | $1,747.5700 |
| 4 | usdc | 0.01% | $9,057,126,161 | $0.9999 |
| 5 | sol | 0.61% | $2,005,420,546 | $81.9200 |


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
