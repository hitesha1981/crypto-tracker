# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-07 02:25 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ansem | 36.08% | $68,271,209 | $0.4185 |
| 2 | edge | 33.50% | $15,802,232 | $0.3189 |
| 3 | rif | 25.81% | $15,607,331 | $0.1304 |
| 4 | grove | 20.07% | $984,507 | $0.0309 |
| 5 | mon | 17.19% | $172,683,382 | $0.0251 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | b | -21.31% | $17,617,558 | $0.1679 |
| 2 | hash | -20.22% | $2,550 | $0.0071 |
| 3 | m | -13.12% | $17,283,248 | $1.2300 |
| 4 | bonk | -9.86% | $113,860,220 | $0.0000 |
| 5 | lab | -8.47% | $71,025,373 | $14.9400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.04% | $59,240,174,123 | $0.9994 |
| 2 | btc | 0.23% | $36,322,393,579 | $63,691.0000 |
| 3 | eth | -0.15% | $16,363,201,766 | $1,783.9600 |
| 4 | usdc | 0.03% | $12,667,969,669 | $1.0000 |
| 5 | sol | 0.25% | $2,559,558,961 | $81.6700 |


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
