prompt_templates = [
    """I am going to show you an email and then ask you questions about it. 

#####

Santiago,
Someone has asked to reset the password for your account. 
If you did not request a password reset, you can disregard this email. 
No changes have been made to your account.
To reset your password, follow this link (or paste into your browser) within the next 90 minutes:
https://www.twilio.com/reset-verification
- Team Twilio

#####

Questions:
1. What is the tl;dr of the email?
2. What is the category of the email (event, class announcement, school announcement, job posting, covid-19 update, or other)?
3. Does the email ask you to do anything?
4. When is the deadline?
5. Does the email mention covid-19?
6. What is the sentiment of the email?
7. What are the key points about the email?

Answers:
1. The tl;dr of the email is that someone has requested a password reset for your account.
2. The category of the email is a password reset.
3. Yes, you need to follow a link to reset your password.
4. The deadline is within the next 90 minutes.
5. No, the email does not mention covid-19.
6. The sentiment of the email is neutral.
7. The key points of the email are that someone has requested a password reset for your account, that I can disregard the email if you did not request a password reset, that no changes have been made to my account, and that you can reset my password by following a link within the next 90 minutes.

#####

{body}

#####

Questions:
1. What is the tl;dr of the email?
2. What is the category of the email (event, class announcement, school announcement, job posting, covid-19 update, or other)?
3. Does the email ask you to do anything?
4. When is the deadline?
5. Does the email mention covid-19?
6. What is the sentiment of the email?
7. What are the key points about the email?

Answers:
1.""",
    """The following is the body of an email I received. I would like you to answer some questions about it after reading it.

#####

{body}

#####

Questions:
1. What is the tl;dr of the email?
2. What are the key points about the email?
3. What is the category of the email (event, class announcement, job posting, covid-19 update, or other)?
4. Is there anything that I need to do?
5. When is the deadline?
6. Does this email mention covid-19?
7. What is the sentiment of the email?

Answers:
1.""",
]

email_examples = {
    "twilio": {
        "type": "other",
        "subject": "Twilio password reset",
        "body": """Santiago,
Someone has asked to reset the password for your account. 
If you did not request a password reset, you can disregard this email. 
No changes have been made to your account.
To reset your password, follow this link (or paste into your browser) within the next 90 minutes:
https://www.twilio.com/reset-verification?key=31420100a67d3983f863140a22a7b2c48ea60696e2cab78bb2e4c3af2dd1492792e928e70a6e00d02326b5b0ccb32e82a09c3429c1154727d70dec8ab79c380ea1540bd3016b9c01f38b0dbe8f0b69038d4b08a0d1eb3cfa3d587f992f96ee8fd03bbc2987d6496077c42529391f2f22568dd5c6c34e27ea6255e199a52c36f544971a70c65726ed58ccd411ec2560a0473a0746e645bc
- Team Twilio""",
    },
    "covid_stay_at_home_lifted": {
        "type": "covid",
        "subject": "Stay-at-home lifted; purple tier in effect",
        "body": """JANUARY 25, 2021
Dear Stanford community,

The State of California lifted its stay-at-home order for all regions of California today, but Santa Clara County and San Mateo County have now returned to the highest-risk purple tier of the state’s COVID-19 framework, which means restrictions on many activities remain in place.

The Regional Stay at Home Order was lifted based on improving projections for intensive care unit capacity. That step returns counties to the state’s framework of color-coded tiers, which are based on numbers of new COVID-19 cases and testing positivity rates in each county. Most of the state, including our local counties, is in the purple “widespread risk” tier.

After the state’s announcement, Santa Clara County also announced today a loosening of some of its previous restrictions, though other county-based restrictions also remain in place.

We are currently assessing how these changes in state and county rules affect university operations. At this point we know the following, and we will provide more details as they become available:

Instruction: Indoor lecture classes are still not permitted. Use of outdoor classrooms and specialized indoor classrooms such as labs and studios is allowed, with adequate physical distancing and capacity limits. Other instruction-related activities such as office hours should continue to be remote wherever possible, and if they cannot be remote, must be conducted outdoors. For details see the In-Person Instructional Recovery Plan.
 
Travel quarantine: Santa Clara County’s travel quarantine remains in place. Anyone who returns to Santa Clara County after traveling more than 150 miles away must quarantine for 10 days. At Stanford, arriving undergraduates also must quarantine for 10 days upon move-in regardless of distance traveled. For Stanford employees working at either the main Stanford campus or Stanford Redwood City, if you travel more than 150 miles from either Santa Clara or San Mateo counties, you should not return to on-site work for 10 days after return.
 
Gatherings: Indoor events and gatherings are still prohibited. However, as Stanford had planned before the stay-at-home order was lifted, registered student households of up to 8 individuals are now allowed for students who arrived on campus by Jan. 10; for students who arrived on campus by Jan. 24, registered households will be allowed Feb. 8. Given this staged introduction of households, the university is not allowing outdoor gatherings of multiple student households at this time, but we plan to begin a process after Feb. 8 that will allow for registered outdoor gatherings that meet state and county rules.
 
Employees: Stanford employees should continue working from home unless approved to be on campus, and those in essential categories should continue to report to work as scheduled. For necessary university business meetings unable to be conducted virtually, outdoors the maximum participation allowed is 15 people; indoors, the maximum is 10 people or 25% of room capacity, whichever is less.
 
Outdoor dining: Dining halls and campus cafes will be allowed to start offering outdoor dining within one’s household later this week, in accord with state and county guidance.
 
Athletics: Santa Clara County is allowing more flexibility for collegiate athletics in the county, with restrictions and safety protocols. Stanford Athletics will be in touch with student-athletes and coaches about the effects on team activities.    
COVID-19 remains dangerous, and adhering to daily public health safeguards continues to be essential to controlling its spread. As the California Department of Public Health said today in announcing the lifting of the stay-at-home order: “It is still critical that Californians continue to wear masks when they leave their homes, maintain physical distance of at least 6 feet, wash their hands frequently, avoid gatherings and mixing with other households, follow all state and local health department guidance, and get the vaccine when it’s their turn.” Updated guidance on choosing a well-fitting face covering is available on the Health Alerts website.

Another state order, the Limited Stay at Home Order, which limited non-essential activities between the hours of 10 p.m. and 5 a.m., also has expired along with the Regional Stay at Home Order.

I hope this information is helpful, and we will continue to provide more information as it becomes available.

Russell Furr
Associate Vice Provost
Environmental Health & Safety""",
    },
    "vaccine_update": {
        "type": "covid",
        "subject": "COVID-19 vaccine update",
        "body": """JANUARY 15, 2021
Dear Stanford community,

I am writing to provide you with an update on COVID-19 vaccination. There has been a great deal of new information from the federal, state and county governments in recent days, and I know that some of it has been confusing.

Here is the latest on what we know:

While public officials set eligibility criteria and phasing for vaccine distribution, local health care providers expand access in accordance with those criteria as sufficient vaccine supply becomes available. For instance, the State of California this week announced that individuals 65 and over are eligible to receive COVID-19 vaccines. However, in Santa Clara County, many health care providers have only been able to expand vaccination to those over the age of 75. California’s vaccine plan is here and the latest update from Santa Clara County is here.
 
Health care workers have been given the highest priority for vaccination. Within our own health care delivery system, all eligible health care workers at Stanford Medicine have now been invited to get vaccinated. Starting today, Stanford Health Care is inviting its patients over the age 75 who reside in Santa Clara and San Mateo counties to receive a vaccination. SHC will continue to provide updates as this information evolves.
 
At this stage of the vaccine rollout, if you believe you are eligible for vaccination, we encourage you to go through your health care provider to confirm eligibility and to schedule an appointment. The latest information on vaccine eligibility through health care providers in Santa Clara County is available here.
 
Later stages of the vaccine rollout will prioritize other age groups and occupations. We are advocating for the needs of our university community in this process. As more specifics become available about the next stages of the vaccine rollout, we will update you.
 
So far, our state and county governments have been focusing on the role of health care providers in administering vaccines. We are awaiting information about the role of educational institutions in vaccine distribution in later stages of the process. This varies from state to state and may also vary from county to county, so you may hear different things from peers and friends at different institutions. In case Stanford is ultimately authorized to provide vaccines to its community, the provost has formed a university-wide COVID-19 Vaccine Governance Committee to develop distribution plans that are in accordance with public health protocols and guided by principles of equity and ethics. The committee is chaired by Judith Goldstein, Faculty Senate chair and professor of political science; Yvonne Maldonado, senior associate dean and professor of global health and infectious diseases in Stanford Medicine; and Niraj Sehgal, chief medical officer for Stanford Health Care and senior associate dean in Stanford Medicine.
These issues have been evolving rapidly in recent days. We will continue to be in touch as there is new information.

Sincerely,

Russell Furr
Associate Vice Provost
Environmental Health & Safety

 

Resources:

State of California: https://covid19.ca.gov/vaccines/#When-can-I-get-vaccinated

Santa Clara County: https://www.sccgov.org/sites/covid19/Pages/COVID19-vaccine-information-for-public.aspx

Stanford Health Care: https://stanfordhealthcare.org/discover/covid-19-resource-center/patient-care/safety-health-vaccine-planning.html""",
    },
    "kea_job": {
        "type": "job",
        "subject": "[cs-students-announce] Engineering job at Kea",
        "body": """See below for job postings at Kea
-----

Launched in 2018, kea is changing the way restaurants operate. We raised an $11M Series A in August 2020 and we're building an amazing team to drive the world’s restaurant commerce. We've experienced 1000% year-over-year revenue growth, and plan to continue that trend by providing even more value for our customers through our technology. There are tens of thousands of restaurants out there that need kea, and we’re building for them.  Our flagship product is an NLP engine to automatically process phone orders. 

We are looking to hire for the following roles: 

Senior Backend Engineer: 
https://kea.breezy.hr/p/712ef6933556-senior-backend-engineer

Engineering Lead:
http://careers.kea.ai/p/59d656d5839a-engineering-lead

Full Stack Engineering Lead
https://kea.breezy.hr/p/aff689828c61-full-stack-lead""",
    },
    "pwr_preferences": {
        "type": "announcement",
        "subject": "PWR Preferences",
        "body": """Good afternoon,

You have been assigned to take your PWR 2 class in Spring quarter. Below, you will find important information on enrolling in a PWR section. The first step is to submit your section preferences. If you will be on leave in Spring, please let us know as soon as possible.

Rank your PWR section preferences (February 14-March 4)

Section Preference Submission Deadline: Thursday, March 4, 5:00 pm PT
Results/Section Assignments Posted by: Sunday, March 7, 5pm PST
How to rank section preferences:
Log in to the PWR Course Assignment website.
Browse the PWR 2 courses in the Catalog; read the course descriptions and watch the course videos. For more information on the instructor, click on their name.
Rank your top seven section preferences. You must list exactly seven sections for your form to be accepted. Each section is independent; if you are interested in both sections taught by the same instructor, you must list both sections in your preferences. Note: You can go back to PWR Course Assignment website and change your preferences up until the deadline for the round.
Submit PWR Section Preferences 
Visit our Enroll page for more information on:
Dates and Deadlines
View or Petition to Change Quarter
Plan for PWR
Submit PWR Section Preferences
Petition to Change PWR Section
View PWR Enrollment FAQs
 
Important: Attendance Policy
If you know you will be absent from either of the first two class meetings of your assigned section, you must contact your instructor and the PWR Office (pwrcourses@stanford.edu) before your scheduled class. Failing to attend any of the first week’s class meetings without making prior arrangements with the PWR Office means that you will automatically be dropped from that section.

Still have questions?
Send any additional questions not answered by this email or our website to pwrcourses@stanford.edu; include your full name and ID number in the message. We’re here to help!

Best wishes,

PWR Office
Open "virtually" 7:00am-4:00pm M-F""",
    },
    "final_study_deadline": {
        "type": "announcement",
        "subject": "Final Study List Deadline is Friday, January 29 @ 5:00pm",
        "body": """Dear Santiago Hernández,

Friday, January 29, 2021 at 5:00 p.m. is the deadline to add and drop classes, or to adjust units on variable unit courses for Winter Quarter.

If you have been manually added as a guest to a class Canvas site, you are not yet enrolled on the official class roster and will not be able to receive a grade or units for your participation. You must add the class in Axess in order to be enrolled. Please ensure your study list below is correct.

The Final Study List Deadline is also the deadline for undergraduates and coterms on undergraduate billing to update enrollment choices between full time and a Flex Term within the quarterly Check-In in Axess.

Your Winter Study List as of: 1/27/2021 11:17 AM


Career
Subject
Catalog #
Section
Component
Description
Grading Basis
Units Taken
Enrollment Status
UG
CS
110
01
LEC
PRINCIPLES OF COMP SYS
Letter (ABCD/NP)
5
Enrolled

The Final Study List deadline is also the last day for tuition reassessment for dropped courses or units. Withdrawing from classes does not reduce your tuition.

Helpful resources for planning your schedule:

Verify that your final exams are not conflicting; check back the week before finals for changes in room assignments: https://registrar.stanford.edu/winter-quarter-exams
Quarter specific enrollment information and deadlines: https://registrar.stanford.edu/news/winter-quarter-enrollment-and-deadlines
Course Catalog: http://explorecourses.stanford.edu. 
All deadlines for the academic year may be found at: https://registrar.stanford.edu/academic-calendar 


Sincerely,

Student Services Center
http://studentservicescenter.stanford.edu""",
    },
    "spring_housing": {
        "type": "announcement",
        "subject": "ACTION NEEDED - Spring Housing Applications Due Tuesday",
        "body": """Dear Santiago,

This is a reminder that we are now accepting spring quarter housing applications within the Housing and Dining Portal in Axess. Students who wish to live in undergraduate housing for spring quarter, including those currently living on campus, must submit an application by 5:00 p.m. on Tuesday, February 16.

You are receiving this email because you are in the junior or senior cohorts we are expecting to be on campus spring quarter or you are in the frosh or sophomore cohort and you have been granted approval through the special circumstances process to live on campus for the spring quarter. 

Your class year for the Spring Housing Allocation process is based on your cohort year, which is the year you first came to Stanford. Your class cohort is Sophomore. 

This email contains important information about what you must do to apply for spring quarter housing and how the Spring Housing Allocation process will work. The housing assignment process for summer quarter has not yet been established. More information will be released as the summer quarter approaches. Please read this letter carefully and in its entirety. Spring Housing Allocation applications are due by 5:00 p.m. on Tuesday, February 16. Spring Housing Allocation dates and other information may change based on evolving developments regarding the COVID-19 pandemic.

Overview
Typically, upperclass students apply for spring housing through a process that is similar to the annual housing Draw. We will not be holding such a process to determine spring quarter assignments. Instead, we will be running a new Spring Housing Allocation process that places a greater emphasis on ensuring friend groups/households can live in the same residence. See below for more information.
To be eligible for housing, you need to be enrolled full time. Juniors and seniors on a flex quarter are only eligible to live on campus if participating in specific full-time approved experiential learning programs.

How does it work?
To participate in the Spring Housing Allocation, students must submit an application in Axess. To submit your application:
Log onto Axess
Select Housing and Dining from the Student menu
Select Apply for Housing to join the Spring Housing Allocation
On your application, you will be able to form a group. Groups can be composed of up to eight students. If you are the leader of your group (the first to apply), you will establish a group name and password and you will rank your group’s housing options in order of preference. You will be required to rank all of the housing options available. Please note that the group you apply with will be considered your initial household. The household program allows for increased social connections between students while still following state and county guidelines. Please visit the Dean of Students website for more information about households.

If you are joining a group, you will enter the name and password established by the group leader. You will not see or be able to rank any housing options. Everyone in the group will have the same housing choices in the same order, as submitted by their group leader. Because of this, it is very important that you are talking with your group members and establishing a consensus regarding the order of your housing choices.

Because our top priority is keeping groups together, randomly generated numbers will not be the sole driver in where you are placed. Your housing rankings and our ability to keep your group together within a house will determine your assignment. Because of this, application numbers and residence cut-offs will not be published.

Why such an emphasis on groups?
Due to the COVID-19 pandemic and the need to ensure physical distancing, it is likely that you will not be able to visit students in other houses. Additionally, students may be restricted to a specific dining hall based on their housing assignment. Because of this, we want to make sure that you are living in close proximity to your friends. 

While the Spring Housing Allocation is designed to keep friend groups together, rest assured it is also perfectly fine to apply without a group. In fact, we anticipate a number of students will elect to apply on their own.

Where can I live?
We have decreased the number of students living in each residence hall to ensure that every student can live in a single (private room), a two-room double (two students sharing occupancy in two rooms), or a 2-bedroom apartment-style unit (each student in a private bedroom and sharing some common areas). Some students assigned to single rooms and 2-room doubles will have extra furniture, since these spaces used to be doubles, triples or quads. We will not be able to remove and store any of the furniture in your room. You are welcome to utilize this extra furniture, but only you are permitted to live in your assigned space. Please note that Mirrielees apartments and the Suites will not be visible on the housing application as they have been set aside for select athletics teams, based on guidance from Santa Clara County on how student athletes should be housed.

In order to help us keep friend groups together, students will rank room types within complexes and large residence halls instead of smaller houses. Depending on demand, houses could be all-frosh, four-class or all upperclass students. The options available on the Spring Housing Allocation application and the number of spaces in each location after staff are assigned can be viewed on the 2020-21 Residence Chart. Please note that not all of the locations will be available for upperclass students, depending on frosh or other assignment needs. Students must rank all of the housing choices on their application. The residences assigned and ultimately occupied will depend on the number of applications received, the number of cancellations after assignments are made and the evolving situation with regard to the COVID-19 pandemic. 
Units in EVGR Building A will have refrigerators and microwaves, but no stoves or ovens. Residence hall rooms will be equipped with minifridges.
Escondido Village Graduate Residences, Building A (EVGR-A)
One of the housing options available to you will be the new Escondido Village Graduate Residences, which opened last fall. The complex is made up of four buildings and undergraduate students will be housed in all of Building A, across the street from the Mirrielees Apartments. 

Every student in EVGR-A will have their own private bedroom and bathroom. Two-bedroom units have common areas of various sizes. Please be sure to see meal plan requirements, below.

Seniors will have top priority for EVGR-A, followed by juniors, then sophomores. If you are in a group with a mix of class years, the group’s priority is determined by the lowest class year. This means if your group is a mix of seniors, juniors, and sophomores, the group will have the sophomore priority for EVGR-A.
""",
    },
    "sg_fellowship": {
        "type": "application",
        "subject": "CS+SG Fellowship Deadline Extended!",
        "body": """Hi all,

We have extended our deadline for the CS + Social Good Spring and Summer Fellowship to be due on Monday, February 15th (11:59pm PT).

We're also hosting more open office hours to answer questions you may have about the fellowship or the application itself. Feel free to book an appointment for Friday, February 12th from 5pm - 9pm PT
or on Sunday ,February 14th from 7am PT-11am PT.

In the meantime, please fill out our application here. 

---

The CS + Social Good Summer Fellowship Program supports Stanford undergraduate students in pursuing at least 9 week projects at the intersection of technology and social impact for Spring and Summer 2021. This year's organization partners are Accountability Counsel, City of San Jose Mayor's Office of Technology and Innovation, Chopra Foundation, Recidiviz, Raheem, and Schoolhouse.world. Students can also design their own fellowship (hot leads list) and apply for funding.

See attached flyer for more information! Feel free to email jnmeltzer@stanford.edu or jmyu@stanford.edu with questions.

Best, 
Jessica and Julia, CS+SG""",
    },
    "cs109_welcome": {
        "type": "class",
        "subject": "[cs109-spr1920-students] Welcome to CS109! Short logistics announcement + survey",
        "body": """Hi everyone,

Welcome to CS109! My name is Lisa, the CS109 instructor for Spring 2020. You are receiving this email because you are currently enrolled in CS109 via Axess.

As you might imagine, the course staff and I are very busy preparing CS109 for this fun and exciting, online-only, S/NC quarter. This involves revamping the course from the ground-up—we're still working on many of the details, but I wanted to share some logistics so far:

(1) We will have online class meetings via Zoom during the scheduled class time: MWF 10:30am, starting Monday, April 6th. All lectures will be recorded in case you cannot attend due to timezones, jobs, family commitments, etc. (but if you can make it, you are encouraged to—it will be fun, I promise).

(2) All non-video resources (announcements, handouts, Gradescope, forum, etc.) will be published as they become available to our public class website: http://cs109.stanford.edu. We will publish a Canvas for storing course videos later this week.

(3) To help us help you, please fill out this survey form (https://forms.gle/ix5ALccLTp2fMzD89) that asks for your timezone, your access to technology, and your course expectations. This form is completely optional and is intended to inform how we can better structure CS109 to meet your learning goals and needs this quarter.

Please email the staff list (cs109@cs.stanford.edu) if you have any additional questions. Thank you and I'm looking forward to our adventure together this quarter!

Lisa Yan""",
    },
    "savvy_class_material": {
        "type": "class",
        "subject": "Material for Wednesday's class: Sp20-OB-110N-01 - Savvy: Learning How to Communicate with Purpose",
        "body": """Hey everyone,

I have a couple items to share with you before class on Wednesday. First, a reminder -- please don't forget to submit Assignment #2 via Canvas by 3pm on Wednesday. I'm looking forward to reading your speech re-writes. Note that I'll be sharing the top submissions with the rest of the class!  Second, our entire class on Wednesday will focus on completing and debriefing a group exercise. Groups will be assigned immediately at the start of class, so please make sure you're on time. Part of what you will need for the class is the attached document.  Don't read this document before class. Rather, print out a copy and have it on hand. If you don't have immediate access to a printer, then just have it on your screen at the start of class and we can figure out a workaround. See you on Wednesday, Professor Flynn
Attached File
Desert Survival Instructions.doc.pdf - 449 KB https://canvas.stanford.edu/courses/119048/files/6040034/download""",
    },
    "savvy_change_in_class": {
        "type": "class",
        "subject": "Introsem -- Change to Wednesday's class!: Sp20-OB-110N-01 - Savvy: Learning How to Communicate with Purpose",
        "body": """Hello everyone,

Wednesday will be our last class session before you deliver your final presentations. As you know, we are planning to discuss two cases in class -- Claude Grunitzky and Donna Dubinsky. Rest assured, we will still be discussing the Grunitzky case, so please read that case before class. I think you'll find it enjoyable. Regarding the Dubinsky case, I've decided to make a change to our syllabus. Instead of discussing communication strategy in a highly politicized workplace, we'll be discussing interventions aimed at improving communication between members of demographically different groups. I'm sure I don't need to tell you what inspired this sudden change to the syllabus, but I hope you welcome it. This topic has a deep history in the field of social psychology. At the start of our session, I'll give a bit of review regarding some of this empirical research, particularly that which focuses on interracial communication. It will be cursory for the most part, given the time constraints and the breadth of the literature. I expect I'll have time to review 5 or 6 pieces of key research. After that review, we'll break into our presentation teams, but rather than "workshop" your presentations, you're going to workshop "intervention" ideas -- something you could do that would increase the rate of, alter the form of, or improve the efficacy of interracial communication (or another form of cross-demographic communication that especially interests you). During the breakout, each of you will have time to share your idea with your teammates. As you explain your idea, you will need to explain not only the specific action to take, but also why this intervention would work. Your classmates can provide feedback on how it can be improved to make it more effective. At the end of this discussion, the team will decide which idea they like the most. When we reconvene, I'll have each group share the idea they selected with the rest of the class. After our session is over, I'll ask one volunteer from each group to send me a one-paragraph summary of the idea, which I'll compile and share with the entire class. Again, the task here is to generate something you could do that would increase the rate of, alter the form of, or improve the efficacy of interracial communication.  You might have some questions about what sort of "intervention" idea you should come up with before class on Wednesday. Well, here are a few things to keep in mind: (1) I'm looking for something you can actually do. Proposing an idea that costs a great deal of money, or requires the cooperation of Oprah Winfrey, will not cut it.  (2) I don't want you to generate an idea for someone else to do. That means i don't want to hear "the government should do this" or "Stanford should do this" or "my roommate should do this." Again, we're interested in what we can implement on our own. (3) The focus must be on communication. After all, that is the subject of this course, and you have gained a great deal of insight that you can now start to apply. As for the form of communication you choose, that is completely up to you. There are countless options. (4) You don't have to come up with this idea on your own. At dinner or in passing conversation with some of your fellow shelterers, bring up the assignment and see if you can solicit good ideas from them or at least use them as a sounding board for your own ideas (side note for Tomas and Santi, and Maddie and Lainey, who are sheltering in place together, you each need separate ideas :).  You have a few days to work on this before Wednesday's class. I hope you give this assignment some serious thought and attention between now and then. There is no grade for this assignment, but that shouldn't matter. The incentive is to use what you have learned in the course to do something meaningful, even if it is only on a small scale. At the moment, communication across demographic boundaries seems to be a significant challenge, for various reasons. That said, it is not an insurmountable challenge. While we may not be able to rehabilitate our entire society through our own individual actions, we can make a start. And that's something. See you on Wednesday, Professor Flynn""",
    },
    "winter_change": {
        "type": "announcement",
        "subject": "Change in our winter undergraduate plan",
        "body": """JANUARY 9, 2021

Dear members of our Stanford community,

We are sending this weekend email to convey an unfortunate but important change in our undergraduate plans for the winter quarter.

After assessing the continuing surge in COVID-19 cases, the lengthening public health restrictions we are under, and how those restrictions likely will affect the on-campus undergraduate experience this quarter, we will not be able to have the frosh and sophomore classes return to campus for the winter quarter, as we had hoped.

Much has changed since early December, when we last updated you on our plans for the quarter. COVID-19 cases in California have skyrocketed. We are now at the worst point of the pandemic so far. Health officials said this week that before Thanksgiving, each day there were 4-5 positive COVID-19 cases per 100,000 population here in Santa Clara County. Recently, it has been approximately 50 cases per 100,000 population – a tenfold increase.

The surge has strained hospitals, leading to alarmingly low capacity in intensive-care units in the Bay Area and most of California and triggering state-mandated stay-at-home orders. Stanford’s hospital is now caring for its largest number of COVID-19 patients during the pandemic, including patients transferred from hospitals in other hard-hit parts of California. 

Amid these circumstances we have proceeded very cautiously as, in the past week, we have welcomed back graduate and professional students, as well as undergraduates with approved special circumstances. The health and safety of our community are, and must be, our top priority. Our expanded student testing program, along with our on-campus safety protocols, are aimed at supporting this critical objective of community health.

However, the worsening COVID-19 circumstances have now eroded our expectations about the experience we could deliver to undergraduates in the winter months. California and Santa Clara County have stringent public health restrictions tied to COVID-19 caseloads. When we carefully evaluated the situation in early December, we estimated that after a two-week arrival delay and a further two-week period of restricted activity, the likely relaxation of public health rules would start to allow more in-person activities, which would make it worthwhile for our frosh and sophomore classes to be on campus. 

Now, the modeling based on the most recent data available to us suggests it is unlikely that our county will be able to move out of California’s highest-risk COVID-19 “purple” tier until late in the winter quarter. That means many restrictions are likely to persist for most of the quarter. Without the ability to expand opportunities for in-person social and academic interaction to the extent we had anticipated, we do not believe we will be able to offer the kind of engaging on-campus student experience that would warrant bringing back the frosh and sophomore classes in their entirety.

We deeply regret having to change plans. We have concluded that doing so is in the best interest of students and our community, though we know many students will be disappointed. We wanted to share this information now, with winter quarter beginning Monday and many students in the frosh and sophomore classes planning to travel to campus two weeks from now.

What is next? Here are some key points:

Classes and student support services will continue to be fully available online, as they were in the fall. The academic continuity team will reach out to instructors who may be impacted by the change to make any adjustments needed.
 
All undergraduates with approved special circumstances, and undergraduate RAs, can continue to be in residence on campus.
 
Since some frosh and sophomores may not have applied to be in residence on the basis of a special circumstance, we will offer a new application period for those students who have not previously applied. Application information is available on a new frequently asked questions web page, referenced below. 
 
This Sunday’s online Winter Convocation for frosh will still occur at 4 p.m. Pacific time, but the Residence Welcomes and House Meetings later in the day will be canceled.
 
We are still planning, in our four-quarter academic year, to invite frosh and sophomores to be on campus for the summer quarter, assuming conditions allow. More information will be provided as soon as it is available.
 
A set of frequently asked questions about the above issues, as well as billing, financial aid and other questions that may be on your minds, has been posted for reference.
To the undergraduate and graduate students who are with us on campus, our commitment to you is undiminished. The university will continue to be in touch with you about the public health situation, and about what may be possible on campus as this quarter progresses. While we saw increased positive cases in our student testing programs this past week as students arrived on campus, we are confident that, with your partnership, we will be able to provide a safe and supportive environment on campus.

And to all students, wherever you are, the faculty and staff of Stanford University continue to be here to support your academic progress and personal wellbeing. We are still in very challenging days, but with the approach of COVID-19 vaccines for wider distribution, there is light at the end of the tunnel. Thank you for your courage and patience on this most unusual journey together.

Sincerely,

Marc Tessier-Lavigne
President

Persis Drell
Provost""",
    },
    "update_undergrad_planning": {
        "type": "announcement",
        "subject": "Update on undergraduate planning",
        "body": """JANUARY 19, 2021

Dear Stanford students,

We hope you are settling well into our winter quarter. These continue to be challenging days, as all of us work through the difficulties posed by the pandemic and the national events that the news brings us each day. We’re grateful for your fortitude, and we hope that the experience of diving back into your academic work is heartening and grounding.

We want to acknowledge one added source of stress for some of you, and that is the change in our undergraduate plans for the winter quarter that we announced on January 9.

Susie Brubaker-Cole and Mona Hicks have been talking with ASSU leadership, and we all have been reviewing the helpful and heartfelt feedback that some students and family members have shared with us directly following this announcement. We made the decision and announcement based on the latest, rapidly evolving conditions, and about two weeks before the frosh and sophomores affected by it would have been traveling to campus. But we’ve heard loud and clear that an earlier final decision would have been much better.

We are always seeking to improve. As such, we’re making adjustments to improve this process for the future. We want to let you know about our thinking:

Winter quarter: First, we want to make sure that undergraduates have seen the accommodations available for winter quarter, which are summarized here and here. The deadline to take a Leave of Absence with a full refund was extended to 5 p.m. today. Sarah Church, our vice provost for undergraduate education, has written to all instructors asking them to be flexible with changes in students’ academic plans. There is information at the links above regarding financial matters and housing. And, again, students who have approved special circumstances are welcome to continue to live on campus this quarter as scheduled.
 
Spring quarter: We in the university are trying our hardest to make it possible for our juniors and seniors to return to campus for a meaningful in-person experience. The changing path of the pandemic and shifting public health rules are what make the timing of final decisions very challenging. For the spring quarter that begins March 29, we continue to plan for juniors and seniors to be in residence, along with undergraduates with approved special circumstances. To facilitate your planning…
 
Timeline: We will provide an update the week of March 1 to confirm our plans for the spring quarter or announce adjustments. We can’t completely eliminate the possibility of a change after that if there are major changes in the public health situation, and we’ll still encourage you to make travel plans that are as flexible as possible. If we see significant risks that might lead to a reversal of the decision, we will let you know with as much specificity as possible at that time. 
 
Decision criteria: The key factors for making a spring quarter decision will be: (1) The public health situation, especially including any limitations on hospital capacity at Stanford and in Santa Clara County. (2) Our ability to ensure the systems and staffing necessary to bring students back safely and to support them on-campus, recognizing the unique needs and demands brought about by the pandemic. (3) The nature of the in-person student experience we are able to offer given the public health rules that we expect to be in effect during the quarter. (As a reminder, it was a change in this third factor – our expectation about the in-person experience we would be able to deliver – that led us to reverse our plans earlier this month.)
 
Student input: We will have a robust engagement process with the ASSU as we approach the spring quarter. In addition to the meetings that already have occurred, we have agreed on an upcoming deep-dive session in which ASSU leaders will help identify issues for the spring quarter and provide input. We’ll also be asking for ASSU input on an ongoing basis as we approach the new quarter. And, we continue to invite input from students directly about your experiences and concerns. Please reach us here with your general suggestions and comments; if you have a personal question, please submit a ServiceNow ticket; and you can reach out to the ASSU at president@assu.stanford.edu or via the assu.stanford.edu website.
This has been a hard period for students, in many ways, and we regret that the timing of the winter decision added to the challenges. We appreciate the grace and resolve with which you are meeting the circumstances before you. This also has been a hard period for the university, as we confront a situation we’ve never faced, with changing dynamics each and every day. As we learn and adjust our approaches, our firm and unchanging goal is to support your educational experience at Stanford, and to do it in the safest way possible.

Thank you for your feedback, and we assure you that we will continue to be in touch.

Sincerely,

Persis Drell
Provost

Susie Brubaker-Cole
Vice Provost for Student Affairs""",
    },
    "greylock_event": {
        "type": "event",
        "subject": "Private Event Invite - 2020 Techfair Offers Meet & Greet; Final Chance to Confirm Mailing Address for Swag",
        "body": """Hi & Happy New Year!
Private Networking Event Invite for Techfair 2020 Offer Recipients:
Want to meet other students who got offers from Techfair 2020 companies? We're hosting a meet & greet next month. This is a great way to expand your network, meet new people, and make the best of a Thursday evening in the Covid-era. When: Feb 18, 2021 05:00 PM Pacific Time (US and Canada) RSVP required: https://greylock.zoom.us/meeting/register/tJEufuGuqz4vHtAMrEDVUsW-MPc4ZHlDh_VI 
Address for Swag: 
Our vendor has finally confirmed the items we selected for swag are ready for shipment in the next two weeks! My inbox got flooded with address change emails last time and it was far too many emails to keep track off. Please help me make sure I have the right address for you by submitting any address changes since Sept 2020 via the google form: https://forms.gle/RCzyRqk8iCKyQCiv9  ​ If you're not sure which address you gave or if I got your address request change, please fill out the form again and I will remove the prior entry. I learned an organizing lesson for next time and promise it will be easier for Techfair 2021. 
FAQs:
I'm living in Canada. Can I get swag? --> Yes. 
I'm living outside of the USA and Canada. Can I get swag? --> We can only send packages to the US and Canada. If you want to put a US friend's address for your items, feel free to do so. Make sure they have access to it in February 2021.
What is the swag? --> IT'S A SURPRISE! I welcome your guesses though.

Yuliya Mykhaylovska (she/her) 
Greylock Partners | University Talent 
connect on Linkedin | yuliya@greylock.com""",
    },
    "stripe_update": {
        "type": "application",
        "subject": "Manuel Santiago Hernandez Gutierrez's next steps with Stripe New York",
        "body": """Hi Manuel Santiago,

Congratulations on completing and doing so well in our technical challenge! We are excited to move you forward with the next steps for our Software Engineering Internship position in ourNew York office during our Summer cohort. The next step will be a virtual one hour technical interview over video conference. To complete this, we ask that you do the following action items:

Complete our mandatory Candidate Questionnaire[0] which you can find via the link at the bottom of this email. These questions are not technical in nature and are just a way for us to get to know you better! Don’t worry, there are no wrong answers, but they are required before we can appropriately action the next steps in our interview process.  
You will be receiving a second email from me directing you to schedule your technical interview through our scheduling tool, Goodtime. There will be instructions in this email on how to complete scheduling your interview. Please be mindful to schedule this sooner rather than later, so you can have maximum access to availability!
We look forward to continuing our interviews with you and will be reaching out to you following the interview with next steps. 

Best,

Lauren Williams""",
    },
    "lumos_job": {
        "type": "job",
        "subject": "[cs-students-announce] Fwd: 🚀 Join an A16Z-backed Startup this Summer",
        "body": """Hey Fam! 👋

Several ex-Stanford peers and I have been building Lumos to redesign the future of identity on the Internet. It's been a crazy ride! We just raised a $5.5m led by Andreessen Horowitz (A16Z) after only a few months of building the product because we saw lots of traction with customers (e.g. Khan Academy, Formlabs, ...) despite being in stealth! 
Here is more info on Lumos & how to apply: https://www.notion.so/Join-Team-Lumos-898833c654f94562b535853bdcc8c30a !

We are still a small team (10 people) but are ready to triple our headcount in the next 12 months. This is the perfect opportunity for you to 1. have lots of ownership 2. get mentorship from the co-founders and founding engineers, 3. enjoy a tight community (life at Lumos is like a continuation of college -- lots of laughs, caring people, hard work, and epic adventures) Feel free to forward this to your friends or other mailing lists. I am incredibly grateful for my experience at university and times are tough! I am here to help however you want me to — regardless of Lumos. Just drop me a line!

Sending lots of positive vibes your way,

Leo

P.S. Every Wednesday at Lumos, one team member shares a funny video. This was the last one (PM vs. Eng): https://www.youtube.com/watch?v=y8OnoxKotPQ. Hope you enjoy 😄


-- 
Leo Mehr
Stanford MS CS '20
linkedin.com/in/leomehr""",
    },
    "pave_job": {
        "type": "job",
        "subject": "Pave (a16z / YC backed Series A co) hiring engineers",
        "body": """Pave (fka Trove) is an Andreessen Horowitz and YC-backed Series A company. It raised a Series A straight out of YCombinator, one of the few companies to have done that, and Marc Andreessen sits on the board as an observer.
 
Pave is seeking to be a comprehensive compensation solution for companies. It provides a suite of tools to plan and communicate total compensation, eliminating confusion around equity and helping employees dream big about their future at their employer. The CEO wrote a write-up on his vision here.
 
Pave is looking to hire both front-end and full-stack engineers. The job descriptions are below.
 
If interested, please email me with your resume at ktan@a16z.com and I’ll make sure they get to the team. They are currently looking for full-time hires, but internship inquiries can be considered.
 
Front-end engineer: Work directly with the product team and customers.
 
Experience/Expertise desired:
– React & TypeScript
– Component libraries & UI systems
– Building iteratively and gathering feedback
 
Full-stack engineer: Strategize with the Pave team about what to build next, then scope and lead development across the stack to deliver end-to-end.
 
Experience/Expertise desired:
– React & TypeScript
– AWS/GCP
– Serverless architectures
– Owning projects end-to-end""",
    },
    "fireside_khosla": {
        "type": "event",
        "subject": "[bases_opportunities] Fireside Chat with Vinod Khosla of Khosla Ventures: February 3 @ 4:15 PM PST",
        "body": """Join ASES for a Fireside Chat with Vinod Khosla of Khosla Ventures! 
Wednesday, February 3rd at 4:15 PM PST
 
 
Vinod will engage us in a conversation about his experience as well as share advice for current and future founders. A couple of startups will have the opportunity to give a 2-minute mock-pitch to Vinod for feedback. If interested, please fill out this form. Please note that even if you are selected, if we run out of time, you are NOT guaranteed to present. 
 
The event is open to ALL Stanford students! If you plan on attending, please RSVP here. We're looking forward to seeing everyone!
 
 
Event Link: 
https://stanford.zoom.us/j/91354426513?pwd=THJ2UFQzSnc1WGFQVnArVllodEo0Zz09
Meeting ID: 913 5442 6513
Password: 171717""",
    },
    "vaccine_update": {
        "type": "covid",
        "subject": "Updates re COVID-19 for 02/12/2021",
        "body": """Vaccine information
Feb 12, 2021 10:35 am
A message to the campus community highlights a new web page that aims to help members of the campus community track the latest information about vaccine distribution.""",
    },
    "reminder_mindsmachines": {
        "type": "class",
        "subject": "Reminders: Minds and Machines",
        "body": """
Hi all,

A few reminders for this week:

1. Readings and videos for Week 10 due TOMORROW

Reading 1: The secret of our success (Henrich) Ch. 1; submit a Reading response on Perusall or Canvas by Thurs 11/19 12 pm PST
Video 1:The Tragedy of the Commons
Video 2:Public Goods Games ; submit a Video response (on Video 1 & 2) by Thurs 11/19 5 pm PST

Video 3: Human cognition; submit a Video response by Thurs 11/19 5 pm PST
Video 4: Why are we polite? Modeling politeness; submit a Video response by Thurs 11/19 5 pm PST
Videos 5A-F (choose TWO to comment on):
Video 5A: Are Group Decisions Consistent? (Emily Hu)
Video 5B: Computer vision for radiology (Josh Kornberg)
Video 5C: The meaning of gradable adjectives (Ciyang Qing)
Video 5D: What's possible with a SymSys degree (Will Kenney)
Video 5E: Examples of interdisciplinary research (David Shacklette)
Video 5F: What the theory theory tells us about schools (Jenny Han)
Submit a Video response on TWO of the 5A-F videos by Thurs 11/19 5 pm PST
2. Module 4 project: See this google doc for more details. Due Friday Nov. 20, at 11:59 pm PST. Make sure to check out the FAQ slides for answers to some questions that have come up!

(If you have not used all of your three penalty-free late days, you can feel free to use them for the project. No need to notify the teaching team, it will be automatically accounted for). 

3. Module 3 project resubmission: For those interested, you may revise and resubmit using this google form, due Sunday Nov. 22, 11:59 pm PST.

Email us, slack, or chat with us during our office hours!

All the best,

Minds and Machines Teaching Team""",
    },
    "cs103_week2": {
        "type": "class",
        "subject": "End of Week 2 announcements",
        "body": """
Hi everyone,

Hope your week 2 is coming to a smooth end and that you'll find some time for rest and recharging this weekend. Here are a few announcements:

MONDAY 5:30pm TUTORIAL CANCELLATION:
Monday is Yom Kippur and Keith will be unavailable for tutorials. Cynthia will be subbing for his 2pm and 7pm tutorials, and the 5:30pm tutorial is cancelled. We apologize for the inconvenience. You may attend any other tutorial on Monday, or plan to do the make-up using the video. 

OFFICE HOURS PROCEDURE:
First save your place in line on QueueStatus, including saying what you want assistance with (e.g., "pset1, 3.ii, 3.iii"). 
When your turn comes up on QueueStatus, join the Zoom call for the staff member set to help you.
Listing your problems accurately allows us to group students with the same questions, and help you all at the same time, effectively allowing you to skip ahead in the queue! And helping students in groups reduces the overall wait times for everyone. You'll sometimes see us take this approach, especially during busier times.

UPCOMING DEADLINES:
Past deadline: pset1 was due today at noon.
Past deadline: week 2 tutorial (make-up) was due today at noon.
Lecture Quiz Week 2 (on the topic of formal logic) is due Monday 9/28 at noon.
Pset 2 just went out and is due in one week Friday 10/2 at noon.
Tutorial Week 3 will be held Monday 9/28, with make-ups due Friday 10/2 at noon.
Midterm Exam 1 will go out on Friday 10/2 at noon, and be due Sunday 10/4 at noon.
Best,
Cynthia and Keith
CS103 Instructors

GIF DU JOUR: (Hope you are feeling supported in this class, virtually) """,
    },
}