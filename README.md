# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-11 02:30 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sui | 21.62% | $2,586,490,813 | $1.3200 |
| 2 | 币安人生 | 14.02% | $56,677,769 | $0.4351 |
| 3 | xec | 12.16% | $97,483,797 | $0.0000 |
| 4 | ub | 11.79% | $13,621,401 | $0.1325 |
| 5 | b | 10.20% | $10,695,899 | $0.4023 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skyai | -12.63% | $43,125,652 | $0.5403 |
| 2 | rave | -9.45% | $18,185,861 | $0.7060 |
| 3 | icp | -6.78% | $106,586,680 | $3.3200 |
| 4 | jto | -6.71% | $54,665,771 | $0.5031 |
| 5 | dash | -6.30% | $99,997,778 | $46.7100 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $61,998,026,290 | $0.9998 |
| 2 | btc | 0.64% | $31,276,995,095 | $81,221.0000 |
| 3 | eth | 1.09% | $18,443,723,049 | $2,349.8600 |
| 4 | usdc | -0.00% | $10,724,378,998 | $0.9998 |
| 5 | sol | 2.77% | $3,743,914,382 | $95.5700 |


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
