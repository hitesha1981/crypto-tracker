# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-16 02:59 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | jto | 29.90% | $257,195,794 | $0.7303 |
| 2 | xlm | 10.89% | $918,626,484 | $0.2093 |
| 3 | spx | 10.85% | $20,549,908 | $0.3800 |
| 4 | aero | 10.48% | $52,529,627 | $0.4147 |
| 5 | zro | 10.07% | $131,680,866 | $1.0820 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -52.58% | $142,700,775 | $0.2509 |
| 2 | beat | -23.59% | $59,369,915 | $4.1900 |
| 3 | gwei | -15.81% | $8,962,007 | $0.1461 |
| 4 | edge | -9.51% | $11,534,495 | $0.3400 |
| 5 | lab | -9.33% | $25,111,222 | $9.5900 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $106,494,427,908 | $0.9994 |
| 2 | btc | 0.44% | $31,851,881,977 | $65,699.0000 |
| 3 | eth | 3.09% | $16,906,280,655 | $1,768.7600 |
| 4 | usdc | 0.00% | $13,994,975,272 | $0.9997 |
| 5 | xrp | 2.88% | $3,085,194,754 | $1.2200 |


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
