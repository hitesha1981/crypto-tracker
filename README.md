# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-28 01:16 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ath | 28.76% | $130,997,695 | $0.0065 |
| 2 | b | 21.44% | $10,876,789 | $0.1711 |
| 3 | lunc | 11.92% | $125,160,508 | $0.0000 |
| 4 | vvv | 11.44% | $36,673,504 | $4.6700 |
| 5 | siren | 7.69% | $17,623,082 | $0.3420 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | power | -25.59% | $29,309,417 | $1.4500 |
| 2 | pippin | -20.08% | $82,674,717 | $0.6373 |
| 3 | stable | -13.21% | $57,772,205 | $0.0330 |
| 4 | sent | -9.28% | $17,018,724 | $0.0225 |
| 5 | zec | -8.18% | $237,238,833 | $219.0300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $70,391,302,918 | $1.0000 |
| 2 | btc | -1.69% | $41,593,716,676 | $65,855.0000 |
| 3 | eth | -3.89% | $20,387,487,967 | $1,930.9100 |
| 4 | usdc | 0.00% | $7,813,026,254 | $0.9999 |
| 5 | sol | -3.91% | $4,051,889,093 | $82.0600 |


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
