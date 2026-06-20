# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-20 02:41 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 83.31% | $67,194,315 | $0.0978 |
| 2 | o | 62.14% | $55,149,261 | $0.8670 |
| 3 | eigen | 20.23% | $74,694,615 | $0.2749 |
| 4 | axs | 16.01% | $80,289,057 | $1.1100 |
| 5 | beat | 15.73% | $70,383,941 | $1.9300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | -37.41% | $56,330,317 | $11.4700 |
| 2 | ub | -28.89% | $17,256,184 | $0.0835 |
| 3 | bill | -10.05% | $22,781,067 | $0.0580 |
| 4 | xlm | -9.02% | $393,724,375 | $0.2113 |
| 5 | kite | -8.23% | $24,887,501 | $0.1683 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $37,867,092,155 | $0.9992 |
| 2 | btc | 0.74% | $22,891,873,253 | $63,344.0000 |
| 3 | usdc | -0.00% | $8,446,281,133 | $0.9999 |
| 4 | eth | 0.12% | $7,438,769,291 | $1,705.0700 |
| 5 | sol | 0.10% | $1,909,260,331 | $69.5400 |


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
