# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-16 02:33 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | anvl | 23.11% | $247,843 | $0.0014 |
| 2 | inj | 20.98% | $253,223,861 | $8.9100 |
| 3 | zro | 19.03% | $181,965,844 | $2.1900 |
| 4 | cards | 18.89% | $16,407,648 | $0.3314 |
| 5 | ake | 18.18% | $37,395,268 | $0.0313 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -20.09% | $21,677,012 | $1.8700 |
| 2 | bdx | -10.45% | $3,184,623 | $0.0738 |
| 3 | jst | -4.43% | $40,901,088 | $0.1328 |
| 4 | cc | -4.08% | $30,376,519 | $0.1056 |
| 5 | dcr | -3.19% | $1,767,062 | $15.2500 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $67,030,446,016 | $0.9990 |
| 2 | btc | 1.69% | $37,010,059,191 | $82,003.0000 |
| 3 | usdc | -0.01% | $20,161,156,752 | $0.9996 |
| 4 | eth | 3.89% | $16,800,460,232 | $2,436.4200 |
| 5 | sol | 3.56% | $3,797,988,721 | $105.2100 |


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
