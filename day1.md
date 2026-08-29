 
PS D:\Agentic> cd Week_1
PS D:\Agentic\Week_1> cd day1
PS D:\Agentic\Week_1\day1> python --version
Python 3.13.1
PS D:\Agentic\Week_1\day1> uv venv --python 3.13.1
uv : The term 'uv' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the 
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ uv venv --python 3.13.1
+ ~~
    + CategoryInfo          : ObjectNotFound: (uv:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS D:\Agentic\Week_1\day1> uv venv --python 3.13.1
Using CPython 3.13.1 interpreter at: C:\Users\hp\AppData\Local\Programs\Python\Python313\python.exe
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate
PS D:\Agentic\Week_1\day1> .\.venv\Scripts\activate.ps1 
(day1) PS D:\Agentic\Week_1\day1> code hello_llm.py
(day1) PS D:\Agentic\Week_1\day1> uv add groq python-dotenv 
error: No `pyproject.toml` found in current directory or any parent
       directory
(day1) PS D:\Agentic\Week_1\day1> uv init
Initialized project `day1`
(day1) PS D:\Agentic\Week_1\day1> uv add groq python-dotenv 
Resolved 16 packages in 847ms
      Built day1 @ file:///D:/Agentic/Week_1/day1                         
Prepared 16 packages in 1.28s
░░░░░░░░░░░░░░░░░░░░ [0/16] Installing wheels...                          warning: Failed to hardlink files; falling back to full copy. This may lead to degraded performance.
         If the cache and target directories are on different filesystems, hardlinking may not be supported.
         If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.
Installed 16 packages in 348ms
 + annotated-types==0.8.0
 + anyio==4.14.2
 + certifi==2026.7.22
 + day1==0.1.0 (from file:///D:/Agentic/Week_1/day1)
 + distro==1.9.0
 + groq==1.6.0
 + h11==0.16.0
 + httpcore==1.0.9
 + httpx==0.28.1
 + idna==3.18
 + pydantic==2.13.4
 + pydantic-core==2.46.4
 + python-dotenv==1.2.2
 + sniffio==1.3.1
 + typing-extensions==4.16.0
 + typing-inspection==0.4.2
(day1) PS D:\Agentic\Week_1\day1> python .\hello_llm.py
Traceback (most recent call last):
  File "D:\Agentic\Week_1\day1\hello_llm.py", line 10, in <module>
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")
ValueError: GROQ_API_KEY environment variable is not set. Please set it in your .env file.
(day1) PS D:\Agentic\Week_1\day1> python .\hello_llm.py
Traceback (most recent call last):
  File "D:\Agentic\Week_1\day1\hello_llm.py", line 10, in <module>
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")
ValueError: GROQ_API_KEY environment variable is not set. Please set it in your .env file.
(day1) PS D:\Agentic\Week_1\day1> python .\hello_llm.py
Traceback (most recent call last):
  File "D:\Agentic\Week_1\day1\hello_llm.py", line 10, in <module>
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")
ValueError: GROQ_API_KEY environment variable is not set. Please set it in your .env file.
(day1) PS D:\Agentic\Week_1\day1> python .\hello_llm.py
python-dotenv could not parse statement starting at line 2
python-dotenv could not parse statement starting at line 4
ChatCompletion(id='chatcmpl-38b5a197-9f04-4c59-a8ed-0b9585f5fcd4', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="In forests deep, where wild things play,\nA tapestry of green, in vibrant sway,\nThe trees stand tall, with leaves of might,\nA gentle breeze, that whispers through the night.\n\nThe sun sets low, in fiery hue,\nPainting the sky, with colors anew,\nThe stars appear, like diamonds bright,\nA celestial show, in all its light.\n\nThe river flows, with gentle stream,\nReflecting the sky, in a peaceful dream,\nThe flowers bloom, in every place,\nA kaleidoscope, of color and grace.\n\nIn nature's beauty, we find our peace,\nA sense of calm, our worries release,\nA connection to, the earth below,\nA feeling of wonder, that forever will grow.", role='assistant', annotations=None, executed_tools=None, function_call=None, reasoning=None, tool_calls=None))], created=1785404647, model='llama-3.3-70b-versatile', object='chat.completion', mcp_list_tools=None, service_tier='on_demand', system_fingerprint='fp_45180df409', usage=CompletionUsage(completion_tokens=148, prompt_tokens=45, total_tokens=193, completion_time=0.418482222, completion_tokens_details=None, prompt_time=0.006143257, prompt_tokens_details=None, queue_time=0.164049681, total_time=0.424625479), usage_breakdown=None, x_groq=XGroq(id='req_01kys6hs2refhvhm1mxrbkdj56', debug=None, seed=103489282, usage=None))
##################################
In forests deep, where wild things play,
A tapestry of green, in vibrant sway,
The trees stand tall, with leaves of might,
A gentle breeze, that whispers through the night.

The sun sets low, in fiery hue,
Painting the sky, with colors anew,
The stars appear, like diamonds bright,
A celestial show, in all its light.

The river flows, with gentle stream,
Reflecting the sky, in a peaceful dream,
The flowers bloom, in every place,
A kaleidoscope, of color and grace.

In nature's beauty, we find our peace,
A sense of calm, our worries release,
A connection to, the earth below,
A feeling of wonder, that forever will grow.
(day1) PS D:\Agentic\Week_1\day1> python .\hello_llm.py
python-dotenv could not parse statement starting at line 2
python-dotenv could not parse statement starting at line 4
##################################
In twilight's hush, where forest dreams,
The trees stand tall, their vigil keeps.
The moon's soft glow, a silver streams,
That dances through the silent deeps.

The stars above, a twinkling show,
Reflected in the lake below,
A mirrored sky, in perfect glow,
A symphony of light and flow.

The world is full, of beauty's might,
In every breeze, a gentle delight,
The scent of blooms, the songs of birds,
A chorus of wonder, that's heard.

In nature's heart, a peace resides,
A sense of calm, where love abides,
A place to breathe, to live, to be,
Connected to the wild, wild sea.
(day1) PS D:\Agentic\Week_1\day1> python .\hello_llm.py
##################################
In twilight's hush, where forest dreams,
A tranquil scene, in silence beams.
The stars above, a twinkling sea,
Reflecting beauty, wild and free.

The trees, like sentinels of old,
Stand guard, their leaves, a gentle fold.
The wind, a whisper, soft and low,
Through petals sways, and scents do flow.

In nature's heart, a beauty lies,
A symphony, that touches the skies.
A dance of light, a chorus of sound,
A harmony, that's always found.

So let us wander, through this land,
And let the beauty, of nature stand.
For in its depths, we find our peace,
And a sense of wonder, that will never cease.
(day1) PS D:\Agentic\Week_1\day1> 