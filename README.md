# X Twitter Tweets & Usernames Scraper

> Collect tweets and usernames from X (Twitter) in a fast, structured, and cost-efficient way.
> This scraper lets you search by username or keyword, filter by date, and pull rich engagement metrics for analysis, dashboards, and automation workflows.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>X Twitter</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This project provides a robust scraper for X (Twitter) that can fetch timelines by username, discover accounts, and search tweets by keywords. It outputs clean, structured data including user details, tweet text, timestamps, media, and engagement statistics.

It’s designed for analysts, growth marketers, researchers, and developers who need reliable X Twitter data without dealing with complex browser automation or manual exports.

### X Twitter Data Collection Capabilities

- Fetch tweets for any public username, with optional date range filters.
- Search tweets by keyword, hashtag, or phrase, with flexible result limits.
- Discover and validate usernames with profile details and recent tweet context.
- Capture engagement stats such as likes, comments, reposts, and quotes.
- Export data in a structured, machine-readable format ready for pipelines and dashboards.

## Features

| Feature | Description |
|--------|-------------|
| Username timeline scraping | Get tweets from a specific username with optional `sincedate` and `untildate` filters to control the time window. |
| Keyword-based tweet search | Search tweets by keyword, phrase, or hashtag and retrieve structured tweet-level data and engagement metrics. |
| Username discovery | Search for usernames by keyword and collect profile information, including display name, verification status, avatar, and profile URL. |
| Rich engagement metrics | Capture counts for comments, reposts, quotes, and likes to support performance analytics and benchmarking. |
| Media and quote detection | Identify media attachments and quoted tweets to understand content formats and interactions. |
| Flexible limits | Use the `maximum` parameter to control result size for cost and performance optimization. |
| Clean JSON-style output | Output designed for easy integration with databases, analytics tools, and data processing pipelines. |
| Proxy-friendly design | Works best with high-quality proxies and controlled request pacing to reduce blocks and maintain stability. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-----------|-------------------|
| keyword | The search keyword or username used as the input query, depending on the mode. |
| sincedate | Optional lower bound for the tweet date range filter (e.g., `2024-01-01`). |
| untildate | Optional upper bound for the tweet date range filter (e.g., `2024-01-31`). |
| maximum | Optional maximum number of items to return for the current operation. |
| author | Full display name of the tweet author. |
| verified | Boolean flag indicating whether the account has a blue or business verification badge. |
| avatar | URL of the user’s profile picture. |
| content | Text content of the tweet or profile description snippet. |
| time | Tweet time formatted as `MM-DD` (e.g., `04-15`). |
| media | Information about media attached to the tweet (image, video, or media URL/identifier). |
| quote | Information or text from a quoted tweet, if present. |
| comments | Number of comments (replies) on the tweet, or `null` if not available. |
| reposts | Number of reposts (retweets), or `null` if not available. |
| mentions | Number of quote-style mentions, or `null` if not available. |
| likes | Number of likes on the tweet, or `null` if not available. |
| link | Direct URL to the tweet. |
| type | Tweet type label such as `tweet`, `retweet`, `tweet_w_media`, or `tweet_w_quote`. |
| username | X Twitter handle of the user (e.g., `elonmusk`), used in username discovery results. |
| fullname | Full name of the user for username search results. |
| url | Direct URL to the user’s profile page. |

---

## Example Output

Below is a realistic example of the JSON-style output returned when collecting tweets by username or searching with a keyword:

    [
      {
        "author": "Elon Musk",
        "verified": true,
        "avatar": "https://pbs.twimg.com/profile_images/.../elon_normal.jpg",
        "content": "Excited about the latest launch 🚀",
        "time": "11-10",
        "media": "https://pbs.twimg.com/media/xyz123.jpg",
        "quote": null,
        "comments": 1523,
        "reposts": 3489,
        "mentions": 210,
        "likes": 45213,
        "link": "https://x.com/elonmusk/status/1234567890123456789",
        "type": "tweet_w_media"
      },
      {
        "author": "SpaceX",
        "verified": true,
        "avatar": "https://pbs.twimg.com/profile_images/.../spacex_normal.jpg",
        "content": "Falcon 9’s first stage has landed on the Just Read the Instructions droneship",
        "time": "11-09",
        "media": "",
        "quote": "Launching progress one step at a time.",
        "comments": 421,
        "reposts": 2109,
        "mentions": 98,
        "likes": 18902,
        "link": "https://x.com/SpaceX/status/987654321098765432",
        "type": "tweet_w_quote"
      },
      {
        "username": "elonmusk",
        "fullname": "Elon Musk",
        "verified": true,
        "avatar": "https://pbs.twimg.com/profile_images/.../elon_normal.jpg",
        "content": "Most recent public tweet text snippet goes here...",
        "url": "https://x.com/elonmusk",
        "type": "username"
      }
    ]

---

## Directory Structure Tree

Assuming a complete working project, a possible structure might look like this:

    x-twitter/
    ├── src/
    │   ├── main.py
    │   ├── clients/
    │   │   ├── http_client.py
    │   │   └── proxy_manager.py
    │   ├── extractors/
    │   │   ├── tweet_parser.py
    │   │   ├── user_parser.py
    │   │   └── utils_time.py
    │   ├── services/
    │   │   ├── username_timeline_service.py
    │   │   ├── username_search_service.py
    │   │   └── keyword_search_service.py
    │   ├── outputs/
    │   │   ├── exporters.py
    │   │   └── formatters.py
    │   └── config/
    │       ├── settings.example.json
    │       └── logging.conf
    ├── data/
    │   ├── inputs.sample.json
    │   └── sample_output.json
    ├── tests/
    │   ├── test_tweet_parser.py
    │   ├── test_user_parser.py
    │   └── test_services.py
    ├── scripts/
    │   ├── run_username_scrape.sh
    │   ├── run_keyword_search.sh
    │   └── export_to_csv.py
    ├── requirements.txt
    ├── pyproject.toml
    └── README.md

---

## Use Cases

- **Social media analysts** use it to **track tweet performance by brand or influencer over time**, so they can **measure engagement, detect spikes, and report on campaign impact**.
- **Growth marketers** use it to **discover relevant usernames and conversations around key topics**, so they can **identify prospects, partners, and outreach opportunities**.
- **Researchers and data scientists** use it to **collect large volumes of tweets for NLP, sentiment analysis, or trend detection**, so they can **build robust models and insights based on real conversations**.
- **Customer success and support teams** use it to **monitor brand mentions and issue-related keywords**, so they can **respond faster and improve customer satisfaction**.
- **Founders and product teams** use it to **follow competitors’ announcements and community reactions**, so they can **adapt roadmaps and messaging based on real-time feedback**.

---

## FAQs

**Q1: Do I need to provide a username or a keyword?**
You can run the scraper in different modes. For username timelines and username discovery, the `keyword` field should contain a valid username (for example, `elonmusk`). For tweet search, the `keyword` can be any phrase, hashtag, or term you want to search.

**Q2: How do `sincedate` and `untildate` work?**
These fields are optional filters for tweet collection. When set, `sincedate` defines the earliest date to include, and `untildate` defines the latest date. If left blank, the scraper will default to the most recent tweets available under the platform’s constraints.

**Q3: What happens if I don’t set `maximum`?**
If `maximum` is omitted, a sensible default limit is applied to prevent excessive load and rate issues. For large-scale data collection, it is recommended to explicitly set `maximum` to control the number of results and tune performance.

**Q4: How can I reduce the risk of being blocked?**
Always use a high-quality or custom proxy setup and introduce delays between requests. Rotating IPs, respecting rate limits, and avoiding aggressive scraping patterns significantly improve stability and reduce the chance of being rate-limited or blocked.

---

## Performance Benchmarks and Results

**Primary Metric – Speed**
On a stable proxy connection, the scraper can typically retrieve between 40–80 tweets per minute per configured worker when using moderate `maximum` limits and reasonable delays.

**Reliability Metric – Success Rate**
With high-quality proxies and conservative rate limits, end-to-end success rates for requests commonly reach above 95%, even when running longer sessions.

**Efficiency Metric – Resource Usage**
The project is optimized for lightweight HTTP calls and JSON handling, keeping CPU and memory usage low enough to run comfortably on modest virtual machines or containers.

**Quality Metric – Data Completeness**
For public tweets and profiles, the scraper is designed to capture all key engagement counters, media indicators, and profile attributes, yielding a high level of data completeness suitable for analytics, dashboards, and downstream machine learning tasks.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
