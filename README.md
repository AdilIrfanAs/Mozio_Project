 
# Mozio Python Backend Project 2.1
Prompt:
* As Mozio expands internationally, we have a growing problem that many transportation suppliers we'd like to integrate cannot give us concrete zip codes, cities, etc that they serve.

* To combat this, we'd like to be able to define custom polygons as their "service area" and we'd like for the owners of these shuttle companies to be able to define and alter their polygons whenever they want, eliminating the need for mozio employees to do this boring grunt work.

Requirement:

1. Build a JSON REST API with CRUD operations for Provider (name, email, phone number, language and currency) and ServiceArea (name, price, geojson information)
2. Create a specific endpoint that takes a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. The name of the polygon, provider's name, and price should be returned for each polygon. This operation should be FAST.
3. Use unit tests to test your API;
4. Write up some API docs (using any tool you see fit);
5. Create a Github account (if you don’t have one), push all your code and share the link with us;
6. Deploy your code to a hosting service of your choice. Mozio is built entirely on AWS, so bonus points will be awarded for use of AWS.

Considerations:
1. All of this should be built in Python/DjangoRest.
2. Use any extra libraries you think will help, choose whatever database you think is best fit for the task, and use caching as you see fit.
3. Ensure that your code is clean, follows standard PEP8 style (though you can use 120 characters per line) and has comments where appropriate.
4. It should take you 8-10 hours to complete and we give you 48 hours to send it back to us.
5.  We will not look at any attachments, screenshots or files sent by you, only Github and your deployed server.

Best of luck,
Jeremias Padilla
Head of Operations
The Mozio Group
