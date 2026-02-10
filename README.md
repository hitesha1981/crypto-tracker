# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-10 01:50 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | axs | 17.56% | $412,857,448 | $1.5600 |
| 2 | stable | 14.31% | $34,243,022 | $0.0221 |
| 3 | rain | 14.08% | $35,413,955 | $0.0104 |
| 4 | hnt | 12.02% | $5,126,735 | $0.9175 |
| 5 | bat | 10.27% | $38,364,779 | $0.1326 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | qrl | -11.68% | $345,254 | $1.9800 |
| 2 | borg | -6.43% | $516,850 | $0.2016 |
| 3 | kas | -5.88% | $19,527,892 | $0.0315 |
| 4 | night | -5.63% | $8,780,100 | $0.0496 |
| 5 | nft | -5.50% | $19,538,529 | $0.0000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $86,617,655,581 | $0.9996 |
| 2 | btc | 0.44% | $54,982,279,409 | $70,392.0000 |
| 3 | eth | 3.03% | $25,164,347,858 | $2,119.4700 |
| 4 | usdc | 0.00% | $8,762,092,195 | $0.9999 |
| 5 | sol | 1.21% | $4,285,135,133 | $87.2800 |


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
