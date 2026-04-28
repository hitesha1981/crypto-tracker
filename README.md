# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-28 02:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bcap | 27.78% | $0 | $105.7500 |
| 2 | xcn | 22.69% | $216,995,533 | $0.0058 |
| 3 | hash | 15.65% | $165,936 | $0.0125 |
| 4 | lunc | 9.14% | $132,022,363 | $0.0001 |
| 5 | chip | 5.78% | $561,367,380 | $0.0770 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | gwei | -24.47% | $10,523,255 | $0.0914 |
| 2 | asteroid | -16.05% | $33,977,449 | $0.0003 |
| 3 | bsb | -15.73% | $79,997,143 | $0.7043 |
| 4 | m | -13.06% | $18,183,171 | $3.7400 |
| 5 | skyai | -12.56% | $16,404,936 | $0.1652 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $63,326,631,906 | $0.9999 |
| 2 | btc | -2.56% | $37,463,050,916 | $77,115.0000 |
| 3 | eth | -3.80% | $16,562,073,043 | $2,299.0900 |
| 4 | usdc | 0.00% | $13,592,300,953 | $0.9999 |
| 5 | sol | -3.70% | $3,527,483,942 | $84.4100 |


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
