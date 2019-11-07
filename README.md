# moviefam

## Background
After spending a fair amount of time looking up for movie recommendations, reading up on recommendation systems (both collaborative and content-based), I decided to try an experiment for recommendations by doing KMeans clustering coupled with cosine similarity. I got a couple of my friends to help me with the frontend-backend dev work which is still in progress?

## Why did I do it?
To try out being able to build an end to end machine learning model which is encapuslated in a service. I also wanted to learn more about gRPC and proto buffers. I had been reading up on how they provide lower latency communication between microservices so decided to try it out. I haven't done any profiling (yet) but hope to do so in the future.

## How is it set up?
We set up a frontend interface with a form with some relevant questions. The questions can be seen in the file (list_of_questions). This form is posted to a GoLang server (fancy, right?). This GoLand server communicated with the recommendation engine microservice (which I wrote in Python woohoo) and the communication takes place via gRPC. It returns a list of titles that the user would enjoy based on the model. 

## Show me the model experiment
It's present in the clean_up_and_analysis notebook in the main directory. 

## What's happening on this in the future?
Nothing really. It was an experiment that is wrapped up now but if I have time, I may make deploy it and make it publicly available? (leave comment on the probability of that happpening lmao)
