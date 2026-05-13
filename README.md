# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-13 02:31 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bill | 27.50% | $294,289,482 | $0.1797 |
| 2 | 币安人生 | 14.58% | $30,102,819 | $0.4306 |
| 3 | ub | 13.65% | $27,514,924 | $0.1716 |
| 4 | chip | 13.25% | $612,264,077 | $0.0689 |
| 5 | inj | 12.41% | $207,418,711 | $5.1000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | vvv | -13.15% | $99,484,678 | $15.4000 |
| 2 | h | -13.15% | $89,373,943 | $0.2367 |
| 3 | lunc | -10.79% | $72,964,189 | $0.0001 |
| 4 | ondo | -8.66% | $272,061,363 | $0.4055 |
| 5 | beat | -8.65% | $6,680,918 | $0.5497 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $57,176,454,230 | $0.9997 |
| 2 | btc | -0.13% | $33,025,914,980 | $81,109.0000 |
| 3 | eth | -0.77% | $14,068,736,683 | $2,294.8500 |
| 4 | usdc | -0.00% | $11,743,980,046 | $0.9998 |
| 5 | sui | -2.12% | $3,421,277,683 | $1.2500 |


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
