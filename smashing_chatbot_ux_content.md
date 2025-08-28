> **Note:** The following article is reproduced verbatim from
> Smashing Magazine, *Google* (2025):
> [Chatbot [[UX](https://design.google/category/ux)](https://design.google/category/ux) – Does Conversation Hurt Or Help?](https://www.smashingmagazine.com/2016/11/does-conversation-hurt-or-help-the-chatbot-ux/)
> for internal educational use only (non-profit).

# Chatbot [[UX](https://design.google/category/ux)](https://design.google/category/ux) – Does Conversation Hurt Or Help?

# Chatbot [[UX](https://design.google/category/ux)](https://design.google/category/ux) – Does Conversation Hurt Or Help?

#### About The Author

#### Email Newsletter

## To Chat Or Not To Chat?

## The Case For Chat

## When You Should Add Conversation To Delight Users

### If You Need To Differentiate From Competition

### If You Need To Handle Edge Conditions

### If You Can Humanize A Brand

## The Case Against Chat

## When You Should Restrict Chat For A Better Chatbot [[UX](https://design.google/category/ux)](https://design.google/category/ux)

### If User Error Would Lead To A Failed Transaction

### If Your Competitive Advantage Is Simplicity

### If You Cannot Easily Handle Unbounded Input

## How Much Should Your Chatbot Chat?

### Further Reading

#### [Smashing Newsletter](https://design.google/the-smashing-newsletter/)

#### Front-End & [[UX](https://design.google/category/ux)](https://design.google/category/ux) Workshops, Online

#### [TypeScript in 50 Lessons](https://design.google/printed-books/)

Mariya is the Head of Design & Engagement at [[[[[[[[[[[[[[TOPBOTS](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com)](https://www.topbots.com), a leading branding & marketing firm specializing in bots, chatbots, and conversational artificial …
[More about
Mariya ↬](https://design.google/author/mariyayao/)

Weekly tips on front-end & [[UX](https://design.google/category/ux)](https://design.google/category/ux).Trusted by 200,000+ folks.

Chatbot fever has infected Silicon Valley. The leaders of virtually every tech giant — including Facebook, Google, Amazon and Apple — proclaim chatbots as the new websites, and messaging platforms as the new browsers. “You should message a business just the way you would message a friend,” declared Mark Zuckerberg when he launched the Facebook Messenger Platform for bots. He and the rest of the tech world are convinced that conversation is the future of business.

But is chatting actually good for bots? Early user reviews of chatbots suggest not. Gizmodo writer Darren Orf [describes](https://gizmodo.com/facebook-messenger-chatbots-are-more-frustrating-than-h-1770732045) Facebook’s chatbot user experiences as “frustrating and useless” and compares using them to “trying to talk politics with a toddler.” His criticisms are not unfair.

Here’s an example of a “conversation” I had with the [1–800-Flowers Messenger bot](https://www.messenger.com/t/1800flowers/) after I became stuck in a nested menu and was unable to return to the main menu. Not exactly a pleasant or productive user experience.

Meet [Smashing Workshops](https://www.smashingconf.com/online-workshops/) on front-end, design & [[UX](https://design.google/category/ux)](https://design.google/category/ux), with practical takeaways, live sessions, video recordings and a friendly Q&A. With Brad Frost, Stéph Walter and [so many others](https://smashingconf.com/online-workshops/workshops).

Designers who are new to conversational interfaces often have the misconception that chatbots must “chat.” At the same time, they underestimate the extraordinary writing skill, technical investment and continual iteration required to implement an excellent conversational user experience ([[UX](https://design.google/category/ux)](https://design.google/category/ux)).

This article explores when conversation benefits and when conversation hurts the chatbot ux (user experience). We’ll walk through case studies for both sides of the argument and compare divergent opinions from Ted Livingston, CEO of Kik, who [advises](https://www.topbots.com/bot-discovery-virality-lessons-kik-ceo-ted-livingston/) bot makers to deprioritize open-ended chat, and Steve Worswick, the creator of “the most human chatbot,” who encourages developers to invest in truly conversational experiences.

As you’ll see from the examples below, both strategies can lead to successful chatbot experiences. The key is to choose the right level of conversational ability for your bot given your business goals, team capabilities and user needs.

Steve Worswick is the developer behind [Mitsuku](https://www.kuki.ai/), one of the world’s most popular chatbots. [Mitsuku](https://www.kuki.ai/) has twice won the [Loebner Prize](https://en.wikipedia.org/wiki/Loebner_Prize), an artificial intelligence award given to the “most human-like chatbot.” The popular chatbot has conversed with more than 5 million users and processed over 150 million total interactions. 80% of [Mitsuku](https://www.kuki.ai/)’s users come back for more chats.

The longest a user has chatted with [Mitsuku](https://www.kuki.ai/) is nine hours in a single day — a testament to the bot’s extraordinary conversational abilities. [Mitsuku](https://www.kuki.ai/) does not help you find makeup products, buy flowers or perform any functional utility. The chatbot’s sole purpose is to provide entertainment and companionship. You won’t be surprised to find out that Worswick thinks “chatbots should be about the chat.”

Building a conversational chatbot that isn’t awful is extremely hard. Worswick nearly gave up many times when [Mitsuku](https://www.kuki.ai/) repeatedly gave unsatisfactory answers and users called her “stupid.” One major breakthrough occurred when Worswick programmed in a massive database with thousands of common objects such as “chair,” “tree” and “cinema,” along with their relationships and attributes.

Suddenly, [Mitsuku](https://www.kuki.ai/) could give sensible answers to strange user questions, such as, “Is a snail slower than a train?” or “Can you eat a tree?” According to Worswick, “Let’s say a user asks [Mitsuku](https://www.kuki.ai/) if a banana is larger than X, but she doesn’t recognize what X is. She knows that a banana is a relatively small object so can deduce that X is probably larger.”

Even if a chatbot is utilitarian, providing spontaneous answers in a conversation — especially if unexpected — can delight and engage users. [Poncho](https://www.messenger.com/t/hiponcho) is a Messenger bot that gives you basic weather reports, but the creators gave the bot the personality of a Brooklyn cat. [Poncho](https://www.messenger.com/t/hiponcho) can conduct small talk and even recognizes other cats. “Weather is boring,” admits [Poncho](https://www.messenger.com/t/hiponcho) founder Kuan Huang. “We make it awesome.”

Making a bot conversational takes tremendous effort, but if you are up to the challenge, here are the top situations in which conversation could distinguish your chatbot from competitors’ and truly delight users.

As seen earlier, [Poncho](https://www.messenger.com/t/hiponcho)’s conversational personality distinguishes the chatty weather cat from boring, routine weather apps. Bots launch at a more rapid pace than mobile apps due to the lower technical barriers to entry. Dozens of bots already exist to service identical use cases, so winners need to stand out with a superior conversational [[UX](https://design.google/category/ux)](https://design.google/category/ux).

Just like weather apps, public transit apps are soulless and boring. We use them out of necessity and not delight. Enter [Bus Uncle](https://www.facebook.com/sgbusuncle/), a bot that can tell you anything you want to know about the Singaporean bus system in his quirky, broken English and suggest funny things to do while you wait.

Comprehensive, detailed guides and maps for the bus system exist on the Internet to help expats and locals find their way home, but [Bus Uncle](https://www.facebook.com/sgbusuncle/)’s conversational interface both simplifies and adds joy to a routine task.

Beware that the bot is not all fun and games. Like any proper Asian uncle, [Bus Uncle](https://www.facebook.com/sgbusuncle/) stays in character by occasionally forcing you to solve math problems.

E-commerce is a challenging space for bots due to product diversity and language variability. Many conversational shopping bots malfunction when users use unrecognized vocabulary or suddenly switch contexts. Such failures are usually technical in nature, where a bot simply doesn’t have the requisite data set or intelligence to handle the edge input.

[ShopBot](https://www.ebayinc.com/stories/news/say-hello-to-ebay-shopbot-beta/) from eBay avoids common e-commerce bot [[UX](https://design.google/category/ux)](https://design.google/category/ux) failures by combining limited option menus with the ability to handle unexpected user input. While many shopping bots hem users into a narrow series of menus, [ShopBot](https://www.ebayinc.com/stories/news/say-hello-to-ebay-shopbot-beta/) was able to quickly adapt when I switched from shopping for jeans to shopping for blouses.

Shopping is a difficult use case for chatbots to master. Superior conversational experiences in e-commerce bots are a function not just of great copy, but of powerful technologies that process natural language, keep track of shoppers’ contexts and preferences, and anticipate diverse needs accurately.

RJ Pittman, chief product officer at eBay, [explains](https://www.ebayinc.com/stories/news/say-hello-to-ebay-shopbot-beta/), “Shoppers have complex needs, which are often not fully met by traditional search engines. The science of AI provides contextual understanding, predictive modeling, and machine learning abilities. Combining AI with eBay’s breadth of inventory and unique selection will enable us to create a radically better and more personal shopping experience.”

Chatting is an intimate act we do with close friends and family, which is why chatting with a “brand” is often an awkward and strange experience. Strong conversational skills in a chatbot can overcome this barrier and establish an authentic connection.

Maintaining a consistent and compelling brand voice in chatbots is not easy. [PullString](https://web.archive.org/web/20190715173217/http://www.pullstring.com/), a conversational AI platform founded by ex-Pixar CTO Oren Jacob, employs an entire department of expert Hollywood screenwriters to bring brands like Mattel’s Barbie and Activision’s Call of Duty to life.

Its demo chatbot, [Jessie Humani](https://www.messenger.com/t/jessiehumani), is powered by over 3,500 lines of carefully selected dialog to create the impression that she’s your messed-up millennial friend who can’t get her life together without your help.

Many bot industry experts believe the word “chatbot” sets the wrong expectation among users that bots should have human-level conversational abilities. The hard reality is that natural-language processing and artificial intelligence still have much progress to make before bots will impress you with their gift of gab.

Ted Livingston, CEO of Kik, a popular messaging platform with a thriving bot store, is squarely on the side of no chatting. “The biggest misconception is that bots need to be about ‘chat.’ What we discovered is that bots that don’t have suggested responses simply don’t work. Users don’t know what to do with an empty input field and a blinking cursor,” he [shared](https://www.topbots.com/bot-discovery-virality-lessons-kik-ceo-ted-livingston/) at a recent bot conference.

Kik started building a conversational platform [two years ago](https://backchannel.com/how-kik-predicted-the-rise-of-chat-bots-2eaf9027b86e#.qwhkcf3ut), long before bots suddenly became cool. In the beginning, its bots allowed freeform responses the same way Facebook Messenger bots do now. What resulted was user confusion and error, as well as complaints from developers about having to deal with the unnecessary complexity of processing open-ended conversation. Kik now restricts user responses to a limited set of predefined options and intentionally makes typing freeform text difficult.

For example, when Sephora’s Kik bot asks what type of beauty products a user would like to see, the bot follows the question with a menu of suggested responses to choose from. A user has to go out of their way to tap “Tap a message” in order to type normally.

There are many cases in which designers of chatbots should restrict conversation to provide a superior experience. Below are a few common situations in which letting users type freeform conversational text complicates development and decreases your bot’s usability.

1–800-Flower’s bot for Facebook Messenger originally gave users three options for flower delivery dates: “Today,” “Tomorrow” or “Choose another date.” The third option allowed users to type in dates freeform, which often resulted in error, confusion and an abandoned or failed transaction.

By removing the third option for users to type in a date manually, 1–800-Flowers actually increased the number of transactions and overall customer satisfaction. Restricting conversation helped it focus on its most important users, the ones who want to send flowers urgently.

[[Chatbots](https://design.google/category/chatbots)](https://design.google/category/chatbots) should give users the key advantage of completing tasks with fewer taps and context switches than regular mobile apps. Enabling open-ended chat can undermine this simplicity and add development complexity related to handling variable input.

An example is the simple meditation bot [Peaceful Habit](https://www.topbots.com/peacefulhabit) for Amazon Echo and Facebook Messenger. The bot is designed to help regular meditators build a daily practice and should be quicker to use than meditation apps.

On the Amazon Echo, a user can start a 5-, 10- or 20-minute meditation completely hands-free, with voice alone. On Facebook Messenger, the bot sends a daily reminder with limited user options, so only a single tap is required to start a meditation practice.

Many user requests appear simple on the surface but are extremely complex to handle in an open-ended conversational interface due to variability of vocabulary, grammatical structures and cultural norms. For example, a user can ask to schedule a meeting by asking any of the following questions:

Turns out the complexity of handling seemingly simple meeting requests requires powerful artificial intelligence capabilities. Several well-funded companies have emerged just to solve narrow scheduling challenges with specialized technology.

When you consider more complex requests, such as asking for restaurant recommendations, limiting conversations often means less confusion for both your bot and your user. [Sure](https://www.messenger.com/t/surebot/), a bot that offers local restaurant recommendations, asks users to type in what they are craving, but it often can’t understand the responses.

By contrast, a similar bot named [OrderNow](https://www.messenger.com/t/ordernowbot) finds local restaurants that deliver and offers a limited menu of cuisines to choose from.

These examples demonstrate that complex artificial intelligence, machine learning or natural-language processing is not required to create a great user experience using a chatbot. As Ted Livingston, CEO of Kik, [warns](https://www.topbots.com/bot-discovery-virality-lessons-kik-ceo-ted-livingston/), “AI is not the killer app for bots. In fact, AI holds most bots back. Bots are just a better way to deliver a software experience. They should do one thing really well.”

How “chatty” your chatbot should be will depend on your users’ mental models of chatbots and the goals and needs your chatbot fulfills for them. Bots on Kik that only offer limited responses can be just as successful and engaging as [Mitsuku](https://www.kuki.ai/) and [Jessie Humani](https://www.messenger.com/t/jessiehumani).

Problems occur when designers do not decide up front who their audience is, how the chatbot fits into their business or brand strategy, what domains the chatbot will and will not cover, and what a successful experience should look like.

When you are deciding how much “conversation” to design into your chatbot experience and are defining the right level of engagement, answer the following questions:

As natural-language understanding, machine learning and artificial intelligence improve, chatbots will inevitably become smarter and more capable in interactions with humans.

For now, just be sure that your bot either sticks with utilitarian offerings or stays within a comfortable zone of conversational topics. Take a cue from how [Mitsuku](https://www.kuki.ai/) gracefully avoids confrontation by excusing herself from a potentially awkward political conversation.

Tips on front-end & [[UX](https://design.google/category/ux)](https://design.google/category/ux), delivered weekly in your inbox. Just the things you can actually use.

With practical takeaways, live sessions, video recordings and a friendly Q&A.

Everything TypeScript, with code walkthroughs and examples. And other printed books.

- [Mariya Yao](https://design.google/author/mariyayao/)
- Nov 24, 2016
- [0 comments](https://design.google#comments-does-conversation-hurt-or-help-the-chatbot-ux)

- 13 min read
- [[UX](https://design.google/category/ux)](https://design.google/category/ux),
[[Communication](https://design.google/category/communication)](https://design.google/category/communication),
[[UI](https://design.google/category/ui)](https://design.google/category/ui),
[[Chatbots](https://design.google/category/chatbots)](https://design.google/category/chatbots)
- Share on [Twitter](https://TwItTeR.CoM/intent/tweet?text=Chatbot%20[UX](https://design.google/category/ux)%20%e2%80%93%20Does%20Conversation%20Hurt%20Or%20Help%3f&url=https%3A%2F%2Fwww.smashingmagazine.com%2f2016%2f11%2fdoes-conversation-hurt-or-help-the-chatbot-ux%2f&via=smashingmag), [LinkedIn](https://data.smashing.services/ball?uri=//www.linkedin.com/shareArticle?url=https://www.smashingmagazine.com%2f2016%2f11%2fdoes-conversation-hurt-or-help-the-chatbot-ux%2f&title=Chatbot%20[UX](https://design.google/category/ux)%20%e2%80%93%20Does%20Conversation%20Hurt%20Or%20Help%3f)

- [SmashingConf Freiburg 2025, September 8–11, 2025](https://smashingconf.com/freiburg-2025/)

- [[UX](https://design.google/category/ux)](https://design.google/category/ux) Strategy in Action, with Susan and Guthrie Weinschenk
- [[UX](https://design.google/category/ux)](https://design.google/category/ux) Strategy Masterclass, with Vitaly Friedman

- [Designing Websites That Convert, with Paul Boag](https://smashingconf.com/online-workshops/workshops/converting-websites-paul-boag/)

- How are you setting user expectations? If you brand your chatbot as a character or a human replacement, users will expect a minimum level of conversational ability. If your bot’s functionality is utilitarian or limited, then guide conversations towards specific outcomes.
- Is your chatbot utilitarian or entertainment-driven? [Mitsuku](https://www.kuki.ai/) is an artificial-intelligence companion, so she’s required to master the art of conversation. On the other hand, a Slackbot that performs SQL queries or pulls CRM data has no need to support chat.
- Does your chatbot reflect your brand’s voice? Major brands such as [Disney](https://www.topbots.com/project/disney-zootopia/) and [Universal Studios](https://www.topbots.com/project/universal-unfriended/) use chatbots to engage audiences beyond simple ad clicks and video views. A chatbot working as a brand ambassador needs to authentically reflect the domain and voice of the company it represents.
- Is your chatbot a familiar service or product? Businesses such as 1–800-Flowers and Domino’s Pizza already have millions of buyers who use their websites, mobile apps and phone numbers to order products. Users who already know what you offer and what they like won’t require as much explanation and hand-holding.
- Does your chatbot need to differentiate itself in a competitive market? Weather apps are a dime a dozen. [Poncho](https://www.messenger.com/t/hiponcho) the Weather Cat differentiates itself by having a distinct personality and delightful reactions, making the bot stand out against other weather services.
- How strong is your technical team and AI platform? Building an adaptable and user-friendly conversational AI is incredibly challenging. Worswick invested over a decade to make [Mitsuku](https://www.kuki.ai/) the award-winning chatbot she is today. Each conversational AI platform has strengths and weaknesses that will affect your chatbot’s [[UX](https://design.google/category/ux)](https://design.google/category/ux).
- How strong is your writing team? In the world of bots, writers are the new designers. Do your writers understand how to write engaging, emotional copy that draws users in? Bots reflect the communication skills of their makers.

- [Conversational Design Essentials: Tips For Building A Chatbot](https://www.smashingmagazine.com/2016/12/conversational-design-essentials-tips-for-building-a-chatbot/)
- [Conversational Interfaces: Where Are We Today? Where Are We Heading?](https://www.smashingmagazine.com/2016/07/conversational-interfaces-where-are-we-today-where-are-we-heading/)
- [Building A Delightful Onboarding Experience For Mobile App Users](https://www.smashingmagazine.com/2016/06/complete-roadmap-building-delightful-onboarding-experience-mobile-app-users/)
- How To Become A [[UX](https://design.google/category/ux)](https://design.google/category/ux) Leader

- [[UX](https://design.google/category/ux)](https://design.google/category/ux)
- [[Communication](https://design.google/category/communication)](https://design.google/category/communication)
- [[UI](https://design.google/category/ui)](https://design.google/category/ui)
- [[Chatbots](https://design.google/category/chatbots)](https://design.google/category/chatbots)