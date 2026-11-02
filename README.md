# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-02 03:44 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | novaai | 11.79% | $703,741 | $0.5713 |
| 2 | trump | 8.96% | $239,689,565 | $1.7300 |
| 3 | strcx | 7.23% | $28,523 | $109.0100 |
| 4 | beam | 6.97% | $145,523,416 | $0.0053 |
| 5 | npc | 6.02% | $3,043,696 | $0.0171 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | -23.10% | $28,248,919 | $0.0070 |
| 2 | rune | -18.42% | $14,913,165 | $0.5087 |
| 3 | awe | -14.92% | $6,871,647 | $0.0624 |
| 4 | xpl | -14.32% | $135,143,625 | $0.0713 |
| 5 | cards | -13.38% | $5,977,384 | $0.2119 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btc | 1.21% | $85,199,023,282 | $78,666.0000 |
| 2 | xaut | 0.67% | $68,936,609,813 | $3,898.2300 |
| 3 | usdt | -0.05% | $29,981,358,623 | $0.9990 |
| 4 | usdc | -0.05% | $7,508,217,438 | $0.9996 |
| 5 | eth | 1.63% | $6,555,540,761 | $2,306.2400 |


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
