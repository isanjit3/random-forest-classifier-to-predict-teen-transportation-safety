# Using a random forest classifier to predict teen transportation safety

This project was created as part of the Community Hackathon at Charles E. Smith Jewish Day School on January 27, 2019.

The team members who worked on this team were Ronoy S., Srujan P, Sanjit T, and Amruth N.

The challenge for this Hackathon was: Improving Independent Travel for Teenagers

Based on this, we decided an important issue to combat with teen travel is safety. We realized that teenagers know that there
are consequences from poor driving, but they don't exactly know how they personally tie into these statistics. So, we wondered, what 
if we could use a machine learning algorithm to predict a users risk of being in an accident based on several factors in a large
dataset? 

After beginning our building stage, we chose to use a random forest classifier. We believed it would be a simple classifier which also 
had greater accuracy than just a simple decision tree. We split into three teams: Ronoy worked on designing the classifier and 
the back-end, Sanjit and Srujan worked on front-end design, and Amruth worked on linking the two and providing general recomendations to both. 

In the end, our classifier was able to use six headers: Age, Gender, People in Car, Experience, Day of Week, Time. Based on a training model we downloaded from the New York government website, we inputted over 850,000 unique data points from a simple csv file into 
Python, and then processed it using the sklearn module. 

For the application, we inputted several data points using textboxes and dropdowns. The website was designed using html, css, java script, and Bootstrap was used for styling and layout. 

In the end our model was able to accurately display the risk of teen drivers. Despite the hackathon being over, we also plan to add a few features to our application to improve it. Specifically...

1) Recommend public transport if higher risk is reported. Set up a map to determine closest locations to do this.
2) Use a location based dataset
3) Improve on front-end design

