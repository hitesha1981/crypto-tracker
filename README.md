# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-21 00:52 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pump | 27.80% | $284,964,714 | $0.0038 |
| 2 | ena | 23.90% | $357,466,166 | $0.1180 |
| 3 | mon | 19.50% | $86,271,301 | $0.0266 |
| 4 | xrp | 15.60% | $6,942,418,237 | $1.2600 |
| 5 | apepe | 14.30% | $12,087,545 | $0.0000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -8.40% | $7,924,029 | $0.0797 |
| 2 | ub | -8.20% | $8,189,095 | $0.1126 |
| 3 | m | -5.60% | $4,192,868 | $1.1800 |
| 4 | trump | -5.60% | $276,878,605 | $1.6500 |
| 5 | kag | -5.60% | $2,019 | $63.0600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $89,993,745,082 | $0.9997 |
| 2 | btc | 5.50% | $55,126,942,274 | $73,756.0000 |
| 3 | eth | 3.60% | $25,551,812,558 | $2,344.7600 |
| 4 | usdc | 0.00% | $22,700,428,145 | $0.9998 |
| 5 | xrp | 15.60% | $6,942,418,237 | $1.2600 |


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
