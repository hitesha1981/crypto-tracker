# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-30 03:20 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | soon | 43.05% | $165,628,860 | $0.4232 |
| 2 | stonk | 28.91% | $37,840,597 | $0.2983 |
| 3 | qnt | 27.86% | $984,463,022 | $293.5200 |
| 4 | btw | 23.45% | $29,928,778 | $1.4000 |
| 5 | zbcn | 22.60% | $14,305,469 | $0.0026 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ai | -15.05% | $42,908,236 | $0.1748 |
| 2 | lit | -14.05% | $189,024,462 | $3.7300 |
| 3 | hbar | -13.25% | $461,451,816 | $0.1030 |
| 4 | shfl | -11.22% | $1,154,231 | $0.5198 |
| 5 | algo | -7.33% | $151,501,624 | $0.1249 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $58,458,049,253 | $0.9996 |
| 2 | btc | 0.30% | $28,301,514,208 | $83,222.0000 |
| 3 | usdc | -0.01% | $18,071,009,271 | $0.9998 |
| 4 | sand | 4.15% | $17,165,141,003 | $0.0439 |
| 5 | eth | 0.33% | $15,483,808,691 | $2,669.1100 |


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
