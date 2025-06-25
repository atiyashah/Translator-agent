from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
from agents.run import RunConfig
import os

load_dotenv()

gemini_api_key =os.getenv("GEMINI_API_KEY")

# step 1 = provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# step 2 = model
model = OpenAIChatCompletionsModel(

    model="gemini-2.0-flash",
    openai_client=provider
     )

# step 3 configration define at run level
run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True

)

# step 4 = create agent
agent = Agent(
    name="Translator agent",
    instructions="you are a helpful translator agent always translate urdu sentence into clear and simple english ",

)
# step 5 = add model to agent
response = Runner.run_sync(

     agent,
     input="میرا نام عطیہ شاہ ہے، میں گزشتہ ایک سال سے GIAIC کی طالبہ ہوں۔ یہاں میں نے فرنٹ اینڈ ڈیویلپمنٹ میں مہارت حاصل کی، اور اس وقت ہم جدید ٹیکنالوجی 'آرٹیفیشل انٹیلیجنس' کی تعلیم حاصل کر رہے ہیں تاکہ مستقبل کے تقاضوں کے مطابق خود کو تیار کر سکیں۔",
     run_config=run_config


)
print(response.final_output)


