# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-18 02:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | grx | 2786.66% | $3,283,435 | $25.5800 |
| 2 | q | 115.83% | $202,420,873 | $0.1361 |
| 3 | anvl | 40.02% | $302,336 | $0.0020 |
| 4 | br | 28.38% | $17,504,939 | $0.4815 |
| 5 | btw | 21.06% | $42,788,330 | $2.4400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | strk | -11.93% | $115,447,781 | $0.0640 |
| 2 | pons | -10.44% | $20,929,128 | $0.2866 |
| 3 | tia | -9.94% | $170,055,251 | $0.6336 |
| 4 | bat | -9.86% | $40,130,920 | $0.1802 |
| 5 | cards | -9.25% | $7,415,338 | $0.2673 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $30,311,291,709 | $0.9992 |
| 2 | btc | 0.25% | $14,655,936,696 | $81,647.0000 |
| 3 | usdc | -0.00% | $8,859,390,891 | $0.9998 |
| 4 | eth | -0.43% | $6,733,976,114 | $2,408.9800 |
| 5 | sol | -0.71% | $1,805,250,183 | $103.6200 |


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
