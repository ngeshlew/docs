> **Note:** The following article is reproduced verbatim from
> Buildo, *Google* (2025):
> [What We Learned From Google’s [People + AI Guidebook]([https://pair.withgoogle.com/guidebook/](https://pair.withgoogle.com/guidebook/))](https://www.buildo.com/blog-posts/what-we-learned-from-googles-people-ai-guidebook)
> for internal educational use only (non-profit).

# What We Learned From Google’s [People + AI Guidebook]([https://pair.withgoogle.com/guidebook/](https://pair.withgoogle.com/guidebook/))

## What is the [People + AI Guidebook]([https://pair.withgoogle.com/guidebook/](https://pair.withgoogle.com/guidebook/))?

## The Solution: Lola, Speech-to-Form Assistant

## The Design Process

### Mapping the user journey with AI opportunities

### Evaluating AI-Driven features for real user benefit

### Defining success criteria for AI-Driven features

### Addressing data challenges

### Ensuring user feedback, control and, graceful failure

## Technical implementation

## What did we learn?

## Bibliography

At Buildo, we believe in hands-on learning through our "Skillo" initiative, where participants' interests and ideas drive learning activities. This approach encourages creativity and curiosity, promotes interaction among diverse individuals, and uncovers shared interests in impactful workplace topics.

In one of our recent Skillo sessions, we became curious about how to design products with AI features. We embarked on a journey to understand the methods and methodologies available today.

During our research, we encountered two significant players in the sector who have invested heavily in this area and developed comprehensive guidelines for designing products and services with AI. Microsoft has created [guidelines for human-AI interaction]([https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/](https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/)), focusing on how humans and AI can work together effectively. Meanwhile, Google offers the [People + AI Guidebook]([https://pair.withgoogle.com/guidebook/](https://pair.withgoogle.com/guidebook/)), a detailed resource that provides best practices and examples for designing with AI.

After thoroughly studying both methodologies, we rolled up our sleeves and put Google's "[People + AI Guidebook]([https://pair.withgoogle.com/guidebook/](https://pair.withgoogle.com/guidebook/))" to the test.

Based on insights from more than a hundred experts, the Guidebook is a comprehensive collection of methods, best practices, and examples for designing with AI, all neatly packed into six chapters:

We aimed to blend this new methodology with our usual product design process. To put it to the test, we picked a project we had already completed and imagined how we could make it even better with AI. We chose a car rental agency project, where employees rent cars to clients all day—a perfect example of a repetitive task that AI could help with. By applying AI, we aimed to make the process smoother, faster, and better for everyone involved.

To put what we learned from Google's Guidebook into action, we embarked on a fun journey to design Lola, our speech-to-form assistant. Designed to make form-filling a more straightforward process, Lola uses AI-driven interactions that make the process faster, easier, and more accurate. The key features we designed for Lola are:

To bring Lola to life, we used our internal design system, [Bento](https://www.bento-ds.com/development), which made crafting her interface smoother and faster. Now that you've met Lola, let's explore how we got here by following the steps in Google's Guidebook!

Our first task was to map out the user journey for the AS-IS process chosen: renting a car online as an agency. Following our standard process, we began by identifying the key elements of the journey:

To incorporate the AI features, we introduced a new layer—identifying AI opportunities at each pain point. This step was key in pinpointing exactly where and how AI could enhance the process, making the overall experience smoother and more efficient.

Next, we took a step back to critically assess whether the AI-driven features we had in mind were genuinely beneficial for users or just adding unnecessary buzz. The Google [People + AI Guidebook]([https://pair.withgoogle.com/guidebook/](https://pair.withgoogle.com/guidebook/)) gave us a [solid framework]([https://pair.withgoogle.com/guidebook/](https://pair.withgoogle.com/guidebook/)chapters) to determine the actual value of these AI features.

We could use Google's template to compare our AI-driven ideas with traditional methods. It helped us identify features that added value. Ultimately, we decided to focus on one particular feature: automatic form-filling from unstructured conversations. And so, Lola, our AI speech-to-form assistant, was born. This feature stood out for its potential to simplify a common task, making everything flow smoother and boosting users' satisfaction.

With our chosen feature—automatic form filling from unstructured conversations—we set out to define clear success criteria to guarantee effectiveness and user satisfaction. Our goal was to leverage AI to eliminate the need for manual input by accurately interpreting user speech and converting it into formal requests to populate a form.

Using Google's format, we framed our success criteria like this:

This method helped us clearly articulate the rationale behind each criterion.

We also identified potential negative impacts and set up action plans. Again, we leaned on Google's format to structure these scenarios:

For example:

By setting positive and negative criteria, we built a [solid framework]([https://pair.withgoogle.com/guidebook/](https://pair.withgoogle.com/guidebook/)chapters) for evaluating the performance of our AI-driven feature. This approach ensured we could celebrate our wins and quickly tackle issues, leading to a more reliable and user-friendly AI experience.

When tackling data-related challenges, teamwork was everything—so I partnered up with my colleague Giovanni. Together, we combined our skills to keep things running smoothly. We worked closely to ensure that the user experience I designed aligned perfectly with the technology's capabilities and interaction modes, all while keeping an eye on the possibilities and limitations. Our teamwork was essential for identifying the core data needs and developing strategies to handle potential issues.

Essential data requirements we focused on included:

While I brought user-centric insights and scenarios, Giovanni applied technical expertise to build solid, reliable solutions. Our collaboration ensured that the AI system was not just effective but also reliable, inclusive, and secure, ultimately leading to a much better user experience.

We also planned for any data disasters that might pop up, like privacy issues, exclusion, or data fragility, and developed solid strategies to tackle them head-on. It was a genuine team effort, and it paid off in creating a more robust and user-friendly system.

A big part of our mission was ensuring users felt in control, keeping their trust and satisfaction front and center. Giovanni and I took the time to outline every event, task, and feature where users needed control, ensuring our approach stayed user-focused. Some of the key features we focused on were:

We also specified the types of feedback (whether implicit or explicit) the system would provide, ensuring users were always in the loop about what Lola was doing. Anticipating and handling errors and failures was also critical to maintaining user trust.

We mapped out potential errors, considered how they might affect users, and planned the best solutions. Whenever something went wrong, users would get clear, straightforward messages explaining what happened and how to fix it—no confusing tech jargon, just easy-to-understand info to avoid frustration.

Introducing AI features like Lola can be challenging. A thoughtful onboarding process is required to help users feel comfortable and confident with the new technology. We aimed to spark curiosity and interest while guiding users step-by-step.

As users become more familiar with Lola, additional features could be introduced progressively, allowing users ample time to adapt and understand each feature thoroughly before encountering new ones.

We put together a proof of concept (POC) to bring our design to life and see if our ideas would actually work. This first POC focused on the core functionality, leaving out some bells and whistles for later. For our tech stack, we used [[OpenAI's](https://openai.com/index/gpt-4/) Whisper](https://openai.com/index/whisper/) and [Assembly AI](https://www.assemblyai.com/) for speech-to-text conversion and [OpenAI's](https://openai.com/index/gpt-4/) GPT-3.5 and GPT-4 for data extraction. This combo gave us the AI muscle we needed to build an intelligent form-filling solution.

The initial POC was a success, with the extracted information placed in the correct fields. We shared an internal demo with our colleagues, which sparked a lot of excitement, questions, and lively discussions about what Lola could do in the future. It was a fantastic way to start the conversation and brainstorm new AI-driven projects—not to mention we had a blast doing it!

Our dive into Google's methodology taught us valuable lessons we're excited to incorporate into our design process. Here are the main takeaways:

By integrating these lessons into our design methodology, we're set to create AI-driven projects that are not only cutting-edge but also deeply human-centered and tuned into users' needs. This approach will help us deliver innovative, valuable, and user-responsive experiences in future projects.

[https://pair.withgoogle.com/guidebook/](https://pair.withgoogle.com/guidebook/)

[https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/](https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/)

[https://adamfard.com/blog/ai-ux-design](https://adamfard.com/blog/ai-ux-design)

[https://www.interaction-design.org/master-classes/how-to-design-with-and-for-artificial-intelligence](https://www.interaction-design.org/master-classes/how-to-design-with-and-for-artificial-intelligence)

[https://www.interaction-design.org/master-classes/ux-design-and-ai](https://www.interaction-design.org/master-classes/ux-design-and-ai)

‍

- Flexible Activation: Get started hands-free with a simple "Hey Lola" or by clicking a button.
- Real-Time Speech Processing: Lola listens and processes speech in real-time, accurately turning words into text and understanding the context.
- Automated Form Population: Automatically populate form fields, reducing manual entry and minimizing errors.
- Information Locking: Lock correct information to prevent overwriting.
- Error Handling and Validation: Ensure mandatory fields are completed, flag errors, and prevent duplicate entries.
- Final Review and Submission: Provide a summary for users to review before submission, ensuring accuracy.

- Actions: The specific steps the agent takes to rent a car for a client, from browsing options to finalizing the rental.
- Actors: The key players in the process—mainly the users themselves.
- Pain Points: The challenges and frustrations users encounter throughout the journey.

- Accuracy: How well the AI can interpret and transcribe spoken language.
- Efficiency: The time saved in filling out forms compared to manually.
- User Satisfaction: Positive feedback from users about their experience with the feature.

- Scenario: If AI's transcription accuracy falls below 90%.
- Action Plan: Review the AI model, update the training data, and retrain to boost accuracy.

- Valid Locations: Make sure the AI can accurately recognize and process location names.
- Open/Close Hours and Available Dates: Ensuring the AI can handle temporal data.
- Correct/Incorrect Input Labels: Clearly define what counts as valid or invalid data entries.

- Manual corrections: Let users manually correct or add information if Lola made a mistake.
- Real-Time Feedback: Giving users immediate feedback on any changes they made.
- Lock Functionality: Allowing users to lock in verified information so it can't be accidentally overwritten.

- [[OpenAI's](https://openai.com/index/gpt-4/) Whisper](https://openai.com/index/whisper/) and [Assembly AI](https://www.assemblyai.com/): These tools provided high-accuracy speech-to-text conversion, allowing Lola to understand and transcribe user speech in real time.
- [OpenAI's](https://openai.com/index/gpt-4/) GPT-3.5 and GPT-4: These advanced AI models did the heavy lifting when it came to understanding context and accurately filling out complex forms.

1. User Needs + Success Definition: Understanding user needs and defining success criteria.
2. Data Collection + Evaluation: Identifying necessary data, sourcing it, and tuning the AI for robustness.
3. Mental Models: Introducing users to the AI system and setting expectations.
4. Explainability + Trust: Explaining the AI system and building user trust through transparency.
5. Feedback + Control: Designing feedback and control mechanisms to enhance performance and user experience.
6. Errors + Graceful Failure: Developing strategies for identifying, diagnosing, and communicating solutions for errors.

1. User research remains essential: Traditional methods are still gold when it comes to understanding users' needs. The challenge now is blending these tried-and-true techniques with new AI methodologies.
2. Teamwork with developers is critical: Working closely with our dev team is vital to maximizing AI technology. This collaboration ensures that AI enhances our projects rather than feeling like a forced fit.
3. Addressing unique challenges: Designing with AI brings its own set of hurdles, like data management and privacy issues. Anticipating these challenges and planning ahead is essential to staying on top of them.
4. Constantly refining our process: To keep AI solutions effective and user-friendly, we must constantly refine our process through iterative testing, gathering user feedback, and continuous improvement.