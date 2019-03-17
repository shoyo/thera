# junction-2019
Official repository for Junction Tokyo 2019 project.  
  
Interact with the app: https://thera-health.herokuapp.com/   
(View on browser for optimal experience)

## Inspiration
Mental illness is a serious societal issue that we believe is not addressed or cared for enough in the modern age. In the United States alone, it is estimated that 1 in 5 adults suffer from a mental illness, and most do not seek treatment. In Japan, this number is estimated to be a staggering proportion of 1 in 4 adults. We believe that a there are two major contributors to the prevalence of mental illnesses. First are the negative social stigmas revolving around mental conditions due to their unpredictability and difficulty in diagnosis. It's difficult to be taken seriously by others when dealing with a mental illness, as its symptoms are difficult to quantify and address. The second is the lack of accessibility for help and coping. Many victims of mental illness lack the ability to vent out their feelings, whether it be due to the lack of support from others or simply being too busy to consult a medical expert. These are the issues Thera, the online resource for dealing with mental illness, aims to address.

## What it does
Thera leverages the power of AI and various APIs (via RapidAPI) to provide necessary help to those suffering a mental condition. In simple terms, Thera is an outlet to cope with the daily struggles of mental illnesses. It allows for a User to vent their thoughts as a journal, which gets run through sentiment and emotion analyses to predict the current mental state of the User. This data is then processed by various APIs to provide the User with media (such as music, a contextually relevant quote, and internet articles) that can improve their mental state and well-being. The user interface of Thera is intuitive, straightforward, and responds directly to the User. For example, if Thera detects that the User's mental state is positive, it renders dynamic, bright, and cheerful backgrounds and recommends various "happy" forms of media. On the other hand, if Thera detects negative or neutral mental states, the interface renders more empathetic color palettes and media recommendations. This design choice reflects the "iso-moodic priciple" in mood management/music theory by Altshuler, which describes how a negative mood cannot be forced to improve with happy music, but rather requires empathetic, compassionate music. Thera also finds medical experts near the User's location with the help of more APIs, and provides direct contact to them for the User. This minimizes the activation barrier for somebody suffering an illness and seeking medical help. Thera is designed from the ground-up to make help as direct and accessible to the User as possible.

## How we built it
Thera is built as a web application deployed with Heroku, with the Python Django framework as the backend, and p5.js, JQuery, HTML, and CSS for the frontend. Github was used to facilitate version control, and several APIs (such as Sentiment/Emotion Analysis) are utilized with the help of Rakuten RapidAPI.

## Challenges we ran into
We encountered several challenges during the development of Thera, especially because this was our first hackathon experience. One particular challenge that stood out was learning to develop code simultaneously in an efficient manner using version control. We eventually adapted to develop code in a modular fashion in order to avoid stepping on each other's toes.

## Accomplishments that we're proud of
We are proud of the fact that despite our lack of experience (and sleep), we were able to put together a project that serves a greater purpose within society. We worked hard with very little sleep are are extremely happy with our final product.

## What we learned
In terms of technical skills, we all improved our understanding of web development and managing several APIs. In terms of "soft" skills, we all learned to cooperate and work effectively even when fatigue starts to take over due to sleep deprivation.

## What's next for Thera
Thera has the potential to become an invaluable tool to those who need it most. Future core features include a robust "journal" system that tracks your day-to-day entries in a helpful way, as well as a chat functionality to talk to/vent to/consult medical experts directly. The recommendations that Thera provides will become more accurate and helpful, and offer suggestions beyond what is currently available.
