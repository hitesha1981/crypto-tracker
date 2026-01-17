# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-17 01:07 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stable | 15.80% | $50,396,700 | $0.0171 |
| 2 | zbcn | 11.64% | $16,050,405 | $0.0034 |
| 3 | 2z | 8.73% | $21,595,799 | $0.1355 |
| 4 | sky | 8.40% | $19,693,789 | $0.0649 |
| 5 | qnt | 8.33% | $19,860,158 | $79.7300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -12.95% | $56,418,481 | $22.8900 |
| 2 | xmr | -10.83% | $351,455,279 | $612.4300 |
| 3 | a7a5 | -6.23% | $4,911 | $0.0118 |
| 4 | cc | -6.12% | $10,867,607 | $0.1267 |
| 5 | icp | -4.62% | $256,281,035 | $4.1400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $62,437,551,216 | $0.9996 |
| 2 | btc | -0.04% | $36,600,739,747 | $95,435.0000 |
| 3 | eth | -0.46% | $23,019,568,876 | $3,290.9900 |
| 4 | usdc | 0.24% | $11,481,417,078 | $1.0020 |
| 5 | sol | 1.46% | $3,948,412,385 | $144.2900 |


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
