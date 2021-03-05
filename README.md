##Landing Page
[https://email-project-d4353e.webflow.io](https://email-project-d4353e.webflow.io)

## Inspiration
When Covid-19 first struck our world, it seemed as if the amount of emails we as students received increased tenfold. Digital communication through emails became even more crucial than ever. Health updates, class deadlines, event links, etc. Everything was online. 

However, we as students have exceeded our capacity to follow and process the amount of information we are receiving. Deadlines from classes became buried between emails.  Important information gets lost, and as a result we are impaired in our ability to live in the new digital world.

As a group, we questioned how we could keep important information accessible. People were spending an unnecessary amount of time reading emails that weren’t important to them. Tree L;DR was created to increase productivity and organization when it comes to digital communication. 

We saw a need for an organized and effective system which allowed students to spend more time focused on the important communication and less time on unimportant mail.

## What it does
Tree L;DR's mission is simple: We want important information to be accessible in an increasingly digital world.

When users sign up for the platform, they submit their phone number, chose email categories and login to their email. After logging into your email, Tree L;DR uses OpenAI's GPT-3 API to summarize and extract relevant information, such as action items and deadlines. Based on the user's chosen preferences, TreeLD;LR will periodically send the user texts. These texts will provide summaries and reminders with regards to the users preferred email categories.

## How we built it
Here is a high-level architecture chart:

![alt text](https://i.ibb.co/Gnz3qmx/TREEL-DR.jpg)

We build a landing page in Webflow to attract users and gather their sign-up information. We then use the Microsoft Identity Platform to let the user sign into their Outlook and acquire an access token for us. We keep the token and store the user information in Google Firestore. Every 5 minutes, a cronjob runs that identifies all of the users whose TreeL;DR digest is due (they can pick 1 hour, 1 day, or 1 week intervals). For each of them, we use the Microsoft GraphQL API to fetch the emails in their Outlook inbox received during the past interval. We extract the text and other information from the email and utilize carefully engineered prompts to summarize, categorize, and process the information from the emails using the OpenAI GPT-3 API. The backend retains all the emails from categories that the user is subscribed to and sends them the compiled TreeL;DR as a text message using the Twilio API. The service is free, but as a sign of their gratitude, users have the ability to give to one of a selected number of charities directly on our landing page, powered by the Checkbook API.

## Challenges we ran into
Our group ran into four main challenges when creating Tree L;DR

1. The first problem we encountered was that most managed Microsoft accounts need approval from an administrator to grant the "Mail.Read" permission for unverified apps. Since the Stanford-managed accounts fall under this category, we had to create our own personal Microsoft accounts to properly demo the program. We submitted the app for review and are waiting to be verified in the next few days, so we can make TreeL;DR accessible for anyone.

2. The second problem we had to overcome was ensuring that that the GPT-3 OpenAI API produced repeatable and consistent output. Because GPT-3 is a general language model, there is no way to programmatically instruct it to do a specific task. Instead, we had to engineer prompts and examples that we send with the email that we want to process, which ended up working great.

3. The third problem we solved was determining how to parse the GPT-3 responses. Because the GPT-3 output is free text, and is therefore unstructured, it was much harder to parse than we had originally predicted. On one hand, we created regexes which were flexible enough to match the format of the text. Then, we added rules for interpreting the sentences in natural language to get a more precise categorical answer.

4. For the sign up process we need to maintain state since we're redirecting the user to Microsoft before they get redirected back to us with their authentication token. Locally, we could do that with a session that uses the file system as a backend but during deployment we discovered that the Google App Engine's file system is read only, making this impossible. We looked at the available options and decided to use the Redis back-end instead, which ended up being a more scalable solution in the long term.

## Accomplishments that we're proud of
We managed to build a fully usable product of great complexity within only 36 hours and dozens of our friends already expressed interest to use it–we are extremely proud of that. Further, we had never used any of the API’s present in our project. For example, no one in our group had ever used OpenAI or Webflow before, and much of Tree L;DR is dependent on those technologies. We had to take the time to learn new technologies from scratch, and we’re really proud of how much our knowledge has grown since beginning this project. 

Secondly, we’re proud of how we were able to find workflow harmony between the members of the group. Every member of the group had a different level of experience with regards to hackathons and creating projects, but we were all able to quickly find our perfect spot on the team. 


## What's next for Tree L;DR
We love Tree L;DR, and we’re so proud of it, but we still have a long way to go with it. Once this hackathon is over, we still have work to do. First, we want to get Tree L;DR verified so that users can sign up using their educational email. Secondly, we want to improve the performance of the app by multi-processing that we can handle large bundles of emails as the same time. Thirdly and finally, we want to improve the experience for the user while on our website. We want to create a whole members portal so that users can properly manage their preferences. 