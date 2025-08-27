> **Note:** The following article is reproduced verbatim from  
> Codecademy Team, *Codecademy* (2025):  
> [Detecting Plagiarism in Generative AI](https://www.codecademy.com/article/detecting-plagiarism-in-generative-ai)  
> for internal educational use only (non-profit).

# Detecting Plagiarism in Generative AI

## Understanding plagiarism in Generative AI

Generative AI (such as ChatGPT from OpenAI) is a helpful tool that can be used to assist us in a variety of tasks ranging from creating cooking recipes to debugging code and even creating an amazing Dungeons and Dragons scenario! But we need to be cognizant that Generative AI can provide plagiarized data. Wait a second…this sounds a lot like the Detecting Hallucinations in Generative AI article. Well, it is.

Similar to Detecting Hallucinations in Generative AI, we must be on the watch for plagiarism when using Generative AI. Plagiarism: the practice of taking someone else's work or ideas and passing them off as one's own. Generative AI plagiarism can be broken up into three categories:

- using generative AI to detect plagiarism
- generative AI plagiarizing content
- detecting generated content

## How to use Generative AI to detect plagiarism

One of the pros of generative AI is using it as a checker to determine if content is plagiarized. For example, if you're a teacher, you can use ChatGPT to determine if an essay your student submitted might contain parts that are plagiarized. Let's see how this works. We will use the first paragraph of Moby Dick and see if ChatGPT can detect that it is plagiarized.

**Prompt:**
```
Can you detect if something is plagiarized?
```

**Response:**
```
I can certainly help you identify potential plagiarism by comparing a given text with publicly available sources up to my knowledge cutoff date in September 2021. However, I am not a dedicated plagiarism detection tool, and my capabilities are limited compared to specialized plagiarism detection software and services.

To detect plagiarism effectively, you should consider using dedicated plagiarism detection tools and services like Turnitin, Copyscape, Grammarly, or specialized software provided by educational institutions or publishers. These tools are designed to compare a given text with a vast database of academic papers, articles, websites, and other sources to identify potential instances of plagiarism.

If you suspect cheating or plagiarism in a text and want to check it, you can copy and paste the text into one of these dedicated tools or services to get a comprehensive plagiarism report. Keep in mind that plagiarism detection tools have varying levels of sensitivity and accuracy, and it's essential to use them in conjunction with your judgment and understanding of plagiarism guidelines.
```

**Prompt:**
```
"""
Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off—then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.
"""
```

**Response:**
```
The passage you've provided is an excerpt from the novel "Moby-Dick" by Herman Melville. This novel was published in 1851 and is in the public domain, which means it can be freely used and quoted without the need for attribution or concerns about plagiarism. If you have any specific questions or need further information about this passage or the book, please feel free to ask.
```

As expected, ChatGPT was able to successfully determine that the paragraph provided was originally authored in Moby Dick.

Remember that ChatGPT only references data up to September 2021. Because of this limitation, we will also discuss other tools we can use to check for plagiarism. Additionally, ChatGPT can only detect plagiarism that it has been trained on. It is possible that ChatGPT, or any generative AI, is unfamiliar with your text.

## How to identify when ChatGPT generates plagiarized content

The next consideration of plagiarism is detecting when ChatGPT generates content that is considered plagiarized. Since generative AI creates content that derives from both prompts and training data, it is possible that generative AI outputs plagiarized content. Let's ask ChatGPT if it plagiarizes and see the output.

**Prompt:**
```
Does generative AI plagiarize?
```

**Response:**
```
Generative AI, like the language model you are currently interacting with, does not inherently plagiarize. Instead, generative AI generates text based on the patterns and information it has learned from the training data it was provided. It can't consciously copy or reproduce specific texts with the intent to plagiarize.

However, the use of generative AI can potentially lead to situations where its generated content resembles existing copyrighted material. In such cases, it's the responsibility of the user to ensure that the content generated by AI complies with copyright and plagiarism guidelines.

To avoid unintentional plagiarism when using generative AI:

1. Review and edit the generated content before using it
2. Ensure that the content is original and doesn't closely resemble existing works
3. Use plagiarism detection tools to check the generated content
4. Provide proper attribution when using AI-generated content
5. Be aware of copyright laws and fair use guidelines

It's important to note that while generative AI can help with content creation, the final responsibility for ensuring originality and avoiding plagiarism lies with the user.
```

## How to detect AI-generated content

The final consideration of plagiarism is detecting when content has been generated by AI. This is particularly important in educational settings where students might be using AI to complete assignments. Let's explore some methods for detecting AI-generated content.

### 1. Using AI Detection Tools

There are several tools available that can help detect AI-generated content:

- **Turnitin**: Popular in educational institutions for detecting both plagiarism and AI-generated content
- **GPTZero**: Specifically designed to detect content generated by GPT models
- **Copyleaks**: Offers AI content detection alongside plagiarism detection
- **Originality.ai**: Focuses on detecting AI-generated content

### 2. Manual Detection Methods

While AI detection tools are helpful, manual methods can also be effective:

**Look for patterns:**
- Unusually consistent writing style
- Lack of personal anecdotes or specific details
- Overly formal or generic language
- Repetitive sentence structures

**Check for inconsistencies:**
- Contradictory information within the same piece
- Inconsistent formatting or style
- Unusual word choices or phrasing

**Analyze the content:**
- Does it lack depth or personal insight?
- Are there specific, verifiable details?
- Does it follow a predictable structure?

### 3. Using ChatGPT to Detect AI-Generated Content

Interestingly, you can also use ChatGPT itself to help detect AI-generated content:

**Prompt:**
```
Can you help me determine if this text was written by AI or a human?
```

**Response:**
```
I can analyze text for characteristics that might indicate AI generation, but I cannot definitively determine authorship. Here are some factors I can consider:

1. **Writing style consistency**: AI-generated text often has very consistent style throughout
2. **Lack of personal details**: AI text typically lacks specific personal experiences or anecdotes
3. **Generic language**: AI may use more generic or formulaic expressions
4. **Structural patterns**: AI-generated content often follows predictable patterns
5. **Factual accuracy**: AI may include factual errors or outdated information

However, these are not foolproof indicators, and the best approach is to use dedicated AI detection tools combined with human judgment.
```

## Best practices for avoiding plagiarism with AI

### 1. Use AI as a Tool, Not a Replacement

- Use AI to generate ideas and outlines, not complete works
- Always review and edit AI-generated content
- Add your own insights, experiences, and voice to the content

### 2. Verify and Attribute

- Fact-check all information provided by AI
- Provide proper citations for any sources referenced
- Use plagiarism detection tools before submitting work

### 3. Understand Your Institution's Policies

- Check your school or organization's policies on AI use
- Be transparent about using AI tools when required
- Follow guidelines for acceptable AI assistance

### 4. Develop Critical Thinking Skills

- Don't rely solely on AI for content creation
- Develop your own writing and research skills
- Use AI to enhance, not replace, your abilities

## Conclusion

Plagiarism in the context of generative AI is a complex issue that requires careful consideration. Whether you're using AI to detect plagiarism, concerned about AI generating plagiarized content, or trying to detect AI-generated content, the key is to remain vigilant and use multiple approaches.

Remember that AI tools are just that—tools. They should enhance your work, not replace your critical thinking and creativity. By understanding the limitations and potential issues with AI-generated content, you can use these powerful tools responsibly and effectively.

The most important thing is to maintain academic integrity and ensure that your work is original, properly attributed, and meets the standards of your institution or organization.
