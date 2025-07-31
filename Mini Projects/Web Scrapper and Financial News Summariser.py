import requests
import feedparser
import asyncio
from telegram import Bot
from telegram.constants import ParseMode
import ollama

# === CONFIG ===
TELEGRAM_BOT_TOKEN = '********hiden for privcy************'
TELEGRAM_CHAT_ID = '@MMANews01'  # Your channel username

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# === SCRAPE ET MARKETS RSS ===
def scrape_et_markets_rss():
    url = "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"
    feed = feedparser.parse(url)

    news_items = []
    for entry in feed.entries[:4]:
        title = entry.title
        link = entry.link
        content = entry.get('summary', entry.get('description', ''))
        if title and content:
            news_items.append((title.strip(), content.strip(), link))
    print(f"✅ Fetched {len(news_items)} items from ET Markets RSS.")
    return news_items

# === SUMMARIZE WITH OLLAMA ===
def summarize_with_ollama(title, content):
    prompt = f"Summarize this financial news in 1-2 lines:\n\nTitle: {title}\n\nContent: {content}"
    try:
        response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content'].strip()
    except Exception as e:
        print(f"⚠️ Ollama error: {e}")
        return content[:300]  # fallback

# === ASYNC TELEGRAM SENDER ===
async def send_news_to_telegram(news_items):
    for title, content, link in news_items:
        print(f"\n➡️ Title: {title}")
        summary = summarize_with_ollama(title, content)
        print(f"💬 Summary: {summary[:80]}...")
        message = f"📢 *{title}*\n\n🧠 _{summary}_\n\n🔗 [Read More]({link})\n\n— _FinBot Daily_"
        try:
            await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode=ParseMode.MARKDOWN)
            print(f"✅ Posted: {title}")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"❌ Telegram post failed: {e}")

# === MAIN ===
async def main():
    print("🔍 Starting bot...")
    news_items = scrape_et_markets_rss()
    if not news_items:
        print("⚠️ No news found. Exiting.")
        return
    await send_news_to_telegram(news_items)

# === RUN ===
if __name__ == '__main__':
    asyncio.run(main())
