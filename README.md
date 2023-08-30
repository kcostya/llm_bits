# Large Language Models

## Summary
This is a collection of notes based on [DeepLearning.Ai](https://www.deeplearning.ai/) Large Language Models (LLM) courses.

### Part 1: ChatGPT Prompt Engineering for Developers
- Principles
  - Write clear and specific instructions
  - Give model time to "think"
- Iterative prompt development
- Capabilities: Summarizing, Inferring, Transforming, Expanding
- Building a chatbot

### Part 2: LangChain for LLM Application Development
- Memory types
  - `ConversationBufferMemory`: allows for storing of messages and then extracts the messages in a variable.
  - `ConversationBufferWindowMemory`: keeps a list of the interactions in the conversation over time, but uses only the last K interactions.
  - `ConversationTokenBufferMemory`: keeps a list of recent interactions in memory, and uses token length rather than number of interactions to determine when to flush interactions.
  - `ConversationSummaryMemory`: creates a summary of the conversation over time.
  - Additional memory types
    - Vector data memory: stores text in a vector database and retrieves the most relevant blocks of text.
    - Entity memories: details about specific entities.

It is possible to combine the memory types (e.g. Conversation memory + Entity memories).
You can also store conversations in conventional databases (such as key-value store or SQL).

To install the OpenAI Python library:
```
!pip install openai
```

The library needs to be configured with your account's secret key, which is available on the [website](https://platform.openai.com/account/api-keys). 

You can either set it as the `OPENAI_API_KEY` environment variable before using the library:
 ```
 !export OPENAI_API_KEY='sk-...'
 ```

Or, set `openai.api_key` to its value:

```
import openai
openai.api_key = "sk-..."
```